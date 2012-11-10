=======
JOSE
======

.. contents::
    :local:



Terms
========

.. glossary::

    Key Material
    Keying Material
        - 鍵の実体のバイト列
        - 「キーとなる素材」

            - 共有キー
            - 初期化ベクター (IV)
            - 別のキーを作る為のマスターキー

    Secret Key Meterial
        - 秘密の :term:`Key Material`

    Non-Secret Key Material
        - 秘密では無い :term:`Key Material`
    
            - 秘密にしない初期化ベクター (IV )

    KDF
    Key Derivation Functions
        - :rfc:`2898`
        - 共有キーから :term:`Secret Key Material` を「派生させる」ために使う関数 ( :ref:`nist-sp-600-56a.5.8`)

    PBKDF
    Password based Key Derivation functions
        - `Appendix B <http://lafoglia.posterous.com/rfc-3962-advanced-encryption-standard-aes-enc>`_  :rfc:`3962` 
        - http://pypi.python.org/pypi/PBKDF
