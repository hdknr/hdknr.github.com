A.3.  Example using response_type=id_token token
------------------------------------------------------------------------

::

  GET /authorize?
    response_type=id_token%20token
    &client_id=s6BhdRkqt3
    &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
    &scope=openid%20profile%20email
    &nonce=n-0S6_WzA2Mj
    &state=af0ifjsldkj HTTP/1.1
  Host: server.example.com

::

  HTTP/1.1 302 Found
  Location: https://client.example.org/cb#
    access_token=jHkWEdUXMU1BwAsC4vtUsZwnNvTIxEl0z9K3vx5KF0Y
    &token_type=Bearer
    &id_token=eyJraWQiOiIxZTlnZGs3IiwiYWxnIjoiUlMyNTYifQ.ewogIml
    zcyI6ICJodHRwOi8vc2VydmVyLmV4YW1wbGUuY29tIiwKICJzdWIiOiAiMjQ
    4Mjg5NzYxMDAxIiwKICJhdWQiOiAiczZCaGRSa3F0MyIsCiAibm9uY2UiOiA
    ibi0wUzZfV3pBMk1qIiwKICJleHAiOiAxMzExMjgxOTcwLAogImlhdCI6IDE
    zMTEyODA5NzAsCiAiYXRfaGFzaCI6ICI3N1FtVVB0alBmeld0RjJBbnBLOVJ
    RIgp9.F9gRev0Dt2tKcrBkHy72cmRqnLdzw9FLCCSebV7mWs7o_sv2O5s6zM
    ky2kmhHTVx9HmdvNnx9GaZ8XMYRFeYk8L5NZ7aYlA5W56nsG1iWOou_-gji0
    ibWIuuf4Owaho3YSoi7EvsTuLFz6tq-dLyz0dKABMDsiCmJ5wqkPUDTE3QTX
    jzbUmOzUDli-gCh5QPuZAq0cNW3pf_2n4zpvTYtbmj12cVcxGIMZby7TMWES
    RjQ9_o3jvhVNcCGcE0KAQXejhA1ocJhNEvQNqMFGlBb6_0RxxKjDZ-Oa329e
    GDidOvvp0h5hoES4a8IuGKS7NOcpp-aFwp0qVMDLI-Xnm-Pg
    &state=af0ifjsldkj

Verifying and decoding the ID Token will yield the following Claims:

.. code-block:: javascript

  {
   "iss": "http://server.example.com",
   "sub": "248289761001",
   "aud": "s6BhdRkqt3",
   "nonce": "n-0S6_WzA2Mj",
   "exp": 1311281970,
   "iat": 1311280970,
   "at_hash": "77QmUPtjPfzWtF2AnpK9RQ"
  }

(draft17)
