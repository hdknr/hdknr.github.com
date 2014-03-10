A.1.7.  Complete Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assemble the final representation: 
The Compact Serialization of this result is the 
string BASE64URL(UTF8(JWE Protected Header)) || '.' ||
BASE64URL(JWE Encrypted Key) || '.' || 
BASE64URL(JWE Initialization Vector) || '.' || 
BASE64URL(JWE Ciphertext) || '.' || 
BASE64URL(JWE Authentication Tag).

The final result in this example (with line breaks for display
purposes only) is:

::

  eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.
  OKOawDo13gRp2ojaHV7LFpZcgV7T6DVZKTyKOMTYUmKoTCVJRgckCL9kiMT03JGe
  ipsEdY3mx_etLbbWSrFr05kLzcSr4qKAq7YN7e9jwQRb23nfa6c9d-StnImGyFDb
  Sv04uVuxIp5Zms1gNxKKK2Da14B8S4rzVRltdYwam_lDp5XnZAYpQdb76FdIKLaV
  mqgfwX7XWRxv2322i-vDxRfqNzo_tETKzpVLzfiwQyeyPGLBIO56YJ7eObdv0je8
  1860ppamavo35UgoRdbYaBcoh9QcfylQr66oc6vFWXRcZ_ZT2LawVCWTIy3brGPi
  6UklfCpIMfIjf7iGdXKHzg.
  48V1_ALb6US04U3b.
  5eym8TW_c8SuK0ltJ3rpYIzOeDQz7TALvtu6UG9oMo4vpzs9tX_EFShS8iB7j6ji
  SdiwkIr3ajwQzaBtQD_A.
  XFBoMYUZodetZdvTiFvSkQ

(draft23)
