==========
OpenSSL
==========


BIGNUM
=========

- 巨大整数を表現する構造体。
- OpenSSLにおいて、MPI(Muliti Precision Integer ) を表現します。

.. automodule:: app.openssl.BIGNUM
    :members:

ECDSA_SIG構造体
==================

- ECDSAの署名の r, s をMPIで保持する構造体

.. automodule:: app.openssl.ECDSA_SIG
    :members:

OpenSSL での ECDSA署名
====================================

ASN.1オブジェクト形式
----------------------------------------

コマンドで行うと、出力はASN.1 Object形式のバイナリストリームです。

.. code-block:: bash

    $ openssl dgst -ecdsa-with-SHA1 -sign server.ecdsa.key data.txt  > data.sig


同じことをM2Cryptoで行うには、 M2Crytpo.EC.EC.sign_dsa_asn1 を使います


.. automodule:: app.openssl.m2crypt_ec_sign
    :members:


C# でBouncyCastle ライブラリを使って SHA256 / ECDSA で署名した場合

ASN.1(わかりやすいように改行と空白入れています)::

    30 46
        02 21 0080CE79C8990BF9CA7926EC621F7026D3EDDB3D73046E07AF237A47D295D732FD
        02 21 00B27370642FA704B158369FF6FC1552A8E2629FFCDB79867FFECD770CBF0AF192

これを、BigIntegerに変換すると

r::

    02210080CE79C8990BF9CA7926EC621F7026D3EDDB3D73046E07AF237A47D295D732FD

s::

    022100B27370642FA704B158369FF6FC1552A8E2629FFCDB79867FFECD770CBF0AF192


このASN.1シグネチャー 0221はおそらく、長さが33バイト(0x21)の整数(0x02)だと思われます。
そして、先頭のバイトは、配列(SEQUECE, 0x30)が後ろに70バイト(0x46)( (33 + 2) x 2= 70 )  
続く、です。

モジュラスr,s の位数
---------------------------------

モジュラスの位数(ビット数)は、曲線のベースポイントに等しいです。

.. list-table::

    * - P-256
      - 256ビット 
      - 32オクテット

    * - P-384
      - 384ビット
      - 48オクテット

    * - P-521
      - 528ビット
      - 66オクテット

