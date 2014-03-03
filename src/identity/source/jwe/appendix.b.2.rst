B.2.  Encrypt Plaintext to Create Ciphertext
------------------------------------------------------

Encrypt the Plaintext 
with AES in Cipher Block Chaining (CBC) mode
using PKCS #5 padding using the ENC_KEY above.  

The Plaintext in this example is:

::

   [76, 105, 118, 101, 32, 108, 111, 110, 103, 32, 97, 110, 100, 32,
   112, 114, 111, 115, 112, 101, 114, 46]

The encryption result is as follows, which is the Ciphertext output:

::

   [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 230, 6,
   75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 33, 215, 104, 143,
   112, 56, 102]


.. note::
    - iv は :ref`jwe.appendix.b.4` をつかってAESを初期化すること

Python
^^^^^^^^^^

.. code-block:: python

    >>> plaintext = [76, 105, 118, 101, 32, 108, 111, 110, 103, 32, 97, 110, 100, 32,
    ...    112, 114, 111, 115, 112, 101, 114, 46]
    >>> 
    >>> plaintext_str = ''.join(chr(i) for i in plaintext)
    >>> plaintext_str
    'Live long and prosper.'
    
    
    >>> cek
    [4, 211, 31, 197, 84, 157, 252, 254, 11, 100, 157, 250, 
     63, 170, 106, 206, 107, 124, 212, 45, 111, 107, 9, 219, 
     200, 177, 0, 240, 143, 156, 44, 207]
    
    >>> mac_key,enc_key = cek[:16],cek[16:]
    >>> mac_key
    [4, 211, 31, 197, 84, 157, 252, 254, 11, 100, 157, 250, 63, 170, 106, 206]
    >>> enc_key
    [107, 124, 212, 45, 111, 107, 9, 219, 200, 177, 0, 240, 143, 156, 44, 207]
    
    >>> iv =[3, 22, 60, 12, 43, 67, 104, 105, 108, 108, 105, 99, 111, 116, 104,
    ...    101]
    
    >>> enc_key_str = ''.join(chr(i) for i in enc_key)
    >>> iv_str = ''.join(chr(i) for i in
    >>> sender = AES.new(enc_key_str, AES.MODE_CBC, iv_str)
    
    >>> pkcs5_pad = lambda BS,s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
    
    >>> p = pkcs5_pad(16, plaintext_str)
    >>> p
    'Live long and prosper.\n\n\n\n\n\n\n\n\n\n'
    
    
    >>> ciphertext_str = sender.encrypt(p)
    >>> ciphertext_str
    '(9S\xb5w!\x85\x94\xc6\xb9\xf3\x18\x98\xe6\x06K\x81\xdf\x7f\x13\xd2R\xb7\xe6\xa8!\xd7h\x
    

    >>> ciphertext = [ord(i) for i in ciphertext_str]
    >>> ciphertext 
    [40, 57, 83, 181, 119, 33, 133, 148, 198, 185, 243, 24, 152, 
     230, 6, 75, 129, 223, 127, 19, 210, 82, 183, 230, 168, 
     33, 215, 104, 143, 112, 56, 102]


復号で確認:

.. code-block:: python

    >>> recipient = AES.new(enc_key_str, AES.MODE_CBC, iv_str)
    >>> p2 = recipient.decrypt(ciphertext_str)
    >>> p2
    'Live long and prosper.\n\n\n\n\n\n\n\n\n\n'
    
    >>> pkcs5_unpad = lambda s : s[0:-ord(s[-1])]
    >>> pkcs5_unpad(p2)
    'Live long and prosper.'
    
    >>> pkcs5_unpad(p2) == plaintext_str
    True
