==========================
ID Token:Implementation
==========================

.. contents:: ID Token Implementation

serialization
====================

base64url without padding
--------------------------------------------------


.. code-block:: python

    import base64 

    def to_base64url(src):
        return base64.urlsafe_b64encode(src).replace('=','') 

    def from_base64url(src):
        return base64.urlsafe_b64decode(src + '=' * (len(src) % 4 ))

id_token
========

Identifiers
--------------

iss
^^^^

- **By** this Issuer, an `id_token`_ is issued.

user_id
^^^^^^^^

- **Of** this User, an `id_token`_ is issued.

aud
^^^^^^^

- **To** this Audience, an `id_token` is issued.


Times
------

iat
^^^^


- Time when a `id_token`_ was created.
- Ellapses seconds from '1970-01-01T0:0:0Z' in UTC, same as `exp`_ 

.. code-block:: python

    >>> import datetime,time
    >>> int( time.mktime( datetime.datetime.utcnow().timetuple() ))
    1336955664

exp
^^^^
    

- Time for issued `id_token`_ to be expired.
- Ellapses seconds from '1970-01-01T0:0:0Z' in UTC


.. code-block:: python

    >>> import datetime,time
    >>> int( time.mktime( (datetime.datetime.utcnow() + datetime.timedelta(minutes=5) ).timetuple() ))
    1336955720    

auth_time
^^^^^^^^^^^

- Time when the User was authenticated at the issuer.
- Ellapses seconds from '1970-01-01T0:0:0Z' in UTC



.. code-block:: python

    import datetime,time
    
    def eseconds(dt) :
        ''' :param dt: datetime  
        '''
        return int( time.mktime( dt.timetuple() ))
        
    def is_valid_time(id_token,check=[],issued_window=300,auth_window=60):
        now = eseconds( datetime.datetime.utcnow() ) 
        check +=[ 
                (  now - issued_window) <=  id_token['iat'] ,       #: Issued Time:Not Too Old
                now >= id_token['iat'],                             #: Issued Time:Older Than Now 
                now <= id_token['exp'] ,                            #: Expired Time:Not Expired
                id_token.has_key('auth_time') == False \
                or (now - issued_window - auth_window <= id_token['auth_time']) #: Auth Time:Not Too Old 
               ]   
        return all(check)


Integrity
-----------

nonce
^^^^^^^

- Generally, http://en.wikipedia.org/wiki/Cryptographic_nonce

    - http://en.wiktionary.org/wiki/nonce

- A random, unique string value used to mitigate replay attacks.
- `nonce`_ MUST be equal to the one provided by Authorization Request.

    - Unique for each Audience.

        - Audience MUST specify unique nonce in the original Authorization Request.
        - Issuer check if there is the existing requested entry for the requesting Audience.


.. code-block:: python

    import string,random,datetime
    
    def random_string(length,chrs =string.ascii_letters + string.digits ):
        ''' generate random string '''
        rnd=random.SystemRandom().randrange
        n=len(chrs) 
        return ''.join([chrs[rnd(n)] for _ in xrange(length)]) 
    
    def make_nonce(when=None,salt_len=):
        ''' elapsed_seconds.microseconds.salt 

            - time factor should be included because requests will be dropped 
              from Audience's database sometime later.
        '''
        when = when if when else datetime.datetime.now()
        return "%x.%x.%s" % ( (int(time.mktime( when.timetuple() ))),
                                when.microsecond ,random_string(salt_len) )

at_hash/c_hash
^^^^^^^^^^^^^^^^^^^

- A proof this `id_token`_ is issued at the same OpenID session 
  when an :term:`access_token` to UserInfo Endpoint 
  or :term:`code` for Access Token Request  was issued.
- **REQUIRED** for the :term:`Implicit Flow`
- creation

    1. provide a hash function specified in the :term:`JWS` header 
       (one of :ref:`Table 3 in JWS specification <jws.table.3>` ):
       one of SHA256,SHA384,SHA512.
    2. generate the hash by the function with the access token/code.
    3. split the hash into 2 byte sequence in the same size
       : left bytes and right bytes
    4. make `base64url without padding`_  of the **left bytes**.


.. code-block:: python

    import hashlib,re

    def make_grant_hash(grant,alg):
        ''' 
            :param grant: access_token or code
            :param alg: alg of JWS header
        '''
        bits=re.search(r'[HRE]S(?P<bits>\d+)$',alg).groupdict()['bits']
        h = getattr(hashlib,"sha%s"%bits)(grant).digest()
        return  to_base64url( h[:len(h)/2])


Conformance
---------------

.. _python.acr:

acr
^^^^

- Authentication Context Class Reference : one in [1,2,3,4]

    - **2** is proper level when an average issuer should consent to ?

- Audiences can register its default `acr`_ preference as :term:`default_acr` via :doc:`reg`.
- If some entity discovers this issuer, 
  the issuer must return the list of `acr`_ in acrs_supported ( :ref:`discovery.table.1` ) of the :doc:`discovery` response .
- Also an audience can specify a required `acr`_ in :term:`OpenID Request Object`. 
- Then the issuer returns `acr`_ in `id_token`_  if `acr`_ was requested.
- Finally the audience checks the `acr`_ in the `id_token`_ .   

Level of Assurance
~~~~~~~~~~~~~~~~~~~~

.. list-table:: LoA 

    *   -   Level
        -   Level Tag
        -   Description

    *   -   1
        -   Low
        -   Little or no confidence in the asserted identity

    *   -   2
        -   Medium
        -   Some confidence in the asserted identity
        
    *   -   3
        -   High
        -   High confidence in the asserted identity 


    *   -   4
        -   Very High
        -   Very high confidence in the asserted identity


ISO29115
~~~~~~~~~~~

.. list-table:: ISO29115 Matrix

    *   -   Item
        -   Level 1
        -   Level 2
        -   Level 3
        -   Level 4

    *   -   Registation
        -   (TBD)
        -   (TBD)
        -   (TBD)
        -   (TBD)

    *   -   Credential Management
        -   (TBD)
        -   (TBD)
        -   (TBD)
        -   (TBD)

    *   -   Authentication Process
        -   (TBD)
        -   (TBD)
        -   (TBD)
        -   (TBD)

Resource
~~~~~~~~~

- Level specified in http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=45138
- http://tools.ietf.org/html/draft-johansson-loa-registry-06


