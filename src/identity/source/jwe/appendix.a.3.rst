A.3.  Example JWE using AES Key Wrap and AES_128_CBC_HMAC_SHA_256
------------------------------------------------------------------------

.. note::
    - :ref:`jwa.5.2.3`

This example encrypts the plaintext "Live long and prosper." 

to the recipient using AES Key Wrap 
for key encryption and AES GCM for content encryption.  


The representation of this plaintext is:

::

   [76, 105, 118, 101, 32, 108, 111, 110, 103, 32, 97, 110, 100, 32,
   112, 114, 111, 115, 112, 101, 114, 46]

.. code-block:: python

    >>> ''.join(chr(i) for i in plaintext)
    'Live long and prosper.'


(draft21)

