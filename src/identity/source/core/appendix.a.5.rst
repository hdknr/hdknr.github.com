A.5.  Example using response_type=code token
------------------------------------------------

::

  GET /authorize?
    response_type=code%20token
    &client_id=s6BhdRkqt3
    &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
    &scope=openid%20profile%20email
    &nonce=n-0S6_WzA2Mj
    &state=af0ifjsldkj HTTP/1.1
  Host: server.example.com

::

  HTTP/1.1 302 Found
  Location: https://client.example.org/cb#
    code=Qcb0Orv1zh30vL1MPRsbm-diHiMwcLyZvn1arpZv-Jxf_11jnpEX3Tgfvk
    &access_token=jHkWEdUXMU1BwAsC4vtUsZwnNvTIxEl0z9K3vx5KF0Y
    &token_type=Bearer
    &state=af0ifjsldkj

(draft17)
