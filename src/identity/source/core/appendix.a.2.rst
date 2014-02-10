A.2.  Example using response_type=id_token
--------------------------------------------------

::

  GET /authorize?
    response_type=id_token
    &client_id=s6BhdRkqt3
    &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
    &scope=openid%20profile%20email
    &nonce=n-0S6_WzA2Mj
    &state=af0ifjsldkj HTTP/1.1
  Host: server.example.com

::

  HTTP/1.1 302 Found
  Location: https://client.example.org/cb#
    id_token=eyJraWQiOiIxZTlnZGs3IiwiYWxnIjoiUlMyNTYifQ.ewogImlz
    cyI6ICJodHRwOi8vc2VydmVyLmV4YW1wbGUuY29tIiwKICJzdWIiOiAiMjQ4
    Mjg5NzYxMDAxIiwKICJhdWQiOiAiczZCaGRSa3F0MyIsCiAibm9uY2UiOiAi
    bi0wUzZfV3pBMk1qIiwKICJleHAiOiAxMzExMjgxOTcwLAogImlhdCI6IDEz
    MTEyODA5NzAsCiAibmFtZSI6ICJKYW5lIERvZSIsCiAiZ2l2ZW5fbmFtZSI6
    ICJKYW5lIiwKICJmYW1pbHlfbmFtZSI6ICJEb2UiLAogImdlbmRlciI6ICJm
    ZW1hbGUiLAogImJpcnRoZGF0ZSI6ICIwMDAwLTEwLTMxIiwKICJlbWFpbCI6
    ICJqYW5lZG9lQGV4YW1wbGUuY29tIiwKICJwaWN0dXJlIjogImh0dHA6Ly9l
    eGFtcGxlLmNvbS9qYW5lZG9lL21lLmpwZyIKfQ.rHQjEmBqn9Jre0OLykYNn
    spA10Qql2rvx4FsD00jwlB0Sym4NzpgvPKsDjn_wMkHxcp6CilPcoKrWHcip
    R2iAjzLvDNAReF97zoJqq880ZD1bwY82JDauCXELVR9O6_B0w3K-E7yM2mac
    AAgNCUwtik6SjoSUZRcf-O5lygIyLENx882p6MtmwaL1hd6qn5RZOQ0TLrOY
    u0532g9Exxcm-ChymrB4xLykpDj3lUivJt63eEGGN6DH5K6o33TcxkIjNrCD
    4XB1CKKumZvCedgHHF3IAK4dVEDSUoGlH9z4pP_eWYNXvqQOjGs-rDaQzUHl
    6cQQWNiDpWOl_lxXjQEvQ
    &state=af0ifjsldkj

The value of the id_token parameter is the ID Token, which is a signed JWT, containing three base64url encoded segments separated by period ('.') characters. The first segment represents the JWT header. Base64url decoding it will result in the following set of Header Parameters:

.. code-block:: javacript

  {"kid":"1e9gdk7","alg":"RS256"}

The alg value represents the algorithm that was used to sign the JWT, in this case RS256, representing RSASSA-PKCS-v1_5 using SHA-256. The kid value is a key identifier used in identifying the key to be used to verify the signature. If the kid value is unknown to the RP, it needs to retrieve the contents of the OP's JWK Set again to obtain the OP's current set of keys.

The second segment represents the Claims in the ID Token. 

Verifying and decoding the ID Token will yield the following Claims:

.. code-block:: javacript

  {
   "iss": "http://server.example.com",
   "sub": "248289761001",
   "aud": "s6BhdRkqt3",
   "nonce": "n-0S6_WzA2Mj",
   "exp": 1311281970,
   "iat": 1311280970,
   "name": "Jane Doe",
   "given_name": "Jane",
   "family_name": "Doe",
   "gender": "female",
   "birthdate": "0000-10-31",
   "email": "janedoe@example.com",
   "picture": "http://example.com/janedoe/me.jpg"
  }

The third segment represents the ID Token signature, which is verified as described in [JWS].

(draft17)
