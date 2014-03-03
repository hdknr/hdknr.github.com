B.6. Compute HMAC Value
----------------------------------------

.. note::

    HS256 = HMAC SHA-256

Compute the HMAC SHA-256 of the concatenated value above.  This result M is:

::

   [83, 73, 191, 98, 104, 205, 211, 128, 201, 189, 199, 133, 32, 38,
   194, 85, 9, 84, 229, 201, 219, 135, 44, 252, 145, 102, 179, 140, 105,
   86, 229, 116]

( https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-21#appendix-B.6 )



python
^^^^^^^^^^

.. code-block:: python


    >>> hmac_input_str = ''.join(chr(i) for i in hmac_input)
    >>> mac_key_str = ''.join(chr(i) for i in mac_key)
    >>> from Crypto.Hash import HMAC
    >>> from Crypto.Hash import SHA256
    >>> hmac = HMAC.new(mac_key_str, hmac_input_str,SHA256)
    >>> hmac
    <Crypto.Hash.HMAC.HMAC instance at 0x2a4e950>
    
    >>> hmac = _
    >>> x = [83, 73, 191, 98, 104, 205, 211, 128, 201, 189, 199, 133, 32, 38,
    ...    194, 85, 9, 84, 229, 201, 219, 135, 44, 252, 145, 102, 179, 140, 105,
    ...    86, 229, 116]
    >>> dig_str = hmac.digest()
    >>> ''.join(chr(i) for i in x ) == dig_str
    True

