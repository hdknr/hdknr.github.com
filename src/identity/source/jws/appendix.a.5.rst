A.5.  Example Plaintext JWS
--------------------------------------------------------

The following example JWS Protected Header declares that the encoded
object is a Plaintext JWS:

::

  {"alg":"none"}

Encoding this JWS Protected Header as BASE64URL(UTF8(JWS Protected
Header)) gives this value:

::

  eyJhbGciOiJub25lIn0

The JWS Payload used in this example, which follows, is the same as
in the previous examples.  Since the BASE64URL(JWS Payload) value
will therefore be the same, its computation is not repeated here.

  {"iss":"joe",
   "exp":1300819380,
   "http://example.com/is_root":true}

The JWS Signature is the empty octet string and 
BASE64URL(JWS Signature) is the empty string.

Concatenating these parts in the order Header.Payload.Signature with
period ('.') characters between the parts yields this complete JWS
(with line breaks for display purposes only):

::

  eyJhbGciOiJub25lIn0
  .
  eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFt
  cGxlLmNvbS9pc19yb290Ijp0cnVlfQ
  .

(draft24)
