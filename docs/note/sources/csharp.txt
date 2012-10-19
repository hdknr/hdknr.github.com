==========
C#
==========

正規表現
========

名付きグループ
---------------

.. code-block:: csharp

     Match m = (new Regex(
            @"^(?<encoded_jws_header>.+)\.(?<encoded_jws_payload>.+)\.(?<encoded_jws_signature>.+)$"
        )).Match(jws_token);
