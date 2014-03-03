========================================================
OAuth 2.0 Form Post Response Mode - draft 01
========================================================

.. note::
    - https://openid.net/specs/oauth-v2-form-post-response-mode-1_0-01.html


.. note::
    - :term:`response_mode`=:term:`form_post` の場合、 :term:`redirect_uri` は別のuriの方がいいかも
        - CSRF の処理を通常のコントローラと別にする必要がある
        - 実際はWebフレームワークでのCSRFを無効にして、 :term:`state` と :term:`nonce` でチェックする。

    - :doc:`クライアント登録 <reg>` で複数の uriを :term:`response_uris`  に登録することになる


