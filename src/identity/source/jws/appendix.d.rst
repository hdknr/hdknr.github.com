Appendix D.  Notes on Key Selection
================================================

This appendix describes a set of possible algorithms 
for selecting the key to be used 
to validate the digital signature or MAC of a JWS object 
or for selecting the key to be used to decrypt a JWE object.

This guidance describes a family of possible algorithms, 
rather than a single algorithm, 
because in different contexts, 
not all the sources of keys will be used, 
they can be tried in different orders,
and sometimes not all the collected keys will be tried; hence,
different algorithms will be used in different application contexts.

The steps below are described for illustration purposes only;
specific applications can and are likely to use different algorithms
or perform some of the steps in different orders.  

Specific applications will frequently have a much simpler method of
determining the keys to use, as there may be one or two key selection
methods that are profiled for the application's use.  

This appendix supplements the normative information on key location in Section 6.

These algorithms include the following steps.  

Note that the steps can be performed in any order 
and do not need to be treated as distinct.  

For example, 
keys can be tried as soon as they are found, 
rather than collecting all the keys before trying any.

1.  Collect the set of potentially applicable keys.  

    Sources of keys may include:

    *  Keys supplied by the application protocol being used.

    *  Keys referenced by the "jku" (JWK Set URL) Header Parameter.

    *  The key provided by the "jwk" (JSON Web Key) Header Parameter.

    *  The key referenced by the "x5u" (X.509 URL) Header Parameter.

    *  The key provided by the "x5c" (X.509 Certificate Chain) Header
       Parameter.

    *  Other applicable keys available to the application.

    The order for collecting and trying keys from different key
    sources is typically application dependent.  

    For example,
    frequently all keys from a one set of locations, such as local
    caches, will be tried before collecting and trying keys from
    other locations.

2.  Filter the set of collected keys.  

    For instance, 
    some applications will use only keys referenced by "kid" (key ID) or
    "x5t" (X.509 certificate SHA-1 thumbprint) parameters.  

    If the application uses the "alg" (algorithm), 
    "use" (public key use), or "key_ops" (key operations) parameters, 
    keys with keys with inappropriate values of those parameters would be excluded.

    Additionally, 
    keys might be filtered to include or exclude keys with certain other member values 
    in an application specific manner.  
    For some applications, 
    no filtering will be applied.

3.  Order the set of collected keys.  

    For instance, keys referenced by "kid" (Key ID) or "x5t" (X.509 Certificate SHA-1 Thumbprint)
    parameters might be tried before keys with neither of these values.  

    Likewise, keys with certain member values might be ordered 
    before keys with other member values.  

    For some applications, no ordering will be applied.

4.  Make trust decisions about the keys.  

    Signatures made with keys not meeting the application's trust criteria 
    would not be accepted.  

    Such criteria might include, but is not limited to the source of the key, 
    whether the TLS certificate validates for keys retrieved from URLs, 
    whether a key in an X.509 certificate is backed by a valid certificate chain, 
    and other information known by the application.

5.  Attempt signature or MAC validation for a JWS object or
    decryption of a JWE object with some or all of the collected and
    possibly filtered and/or ordered keys.  

    A limit on the number of keys to be tried might be applied.  

    This process will normally terminate following a successful validation or decryption.

Note that it is reasonable for some applications to perform signature
or MAC validation prior to making a trust decision about a key, since
keys for which the validation fails need no trust decision.

(draft27)
