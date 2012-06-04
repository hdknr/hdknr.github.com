# -*- coding: utf-8 -*-

'''

.. code-block:: c

    typedef struct ECDSA_SIG_st
        {   
        BIGNUM *r; 
        BIGNUM *s; 
        } ECDSA_SIG;


'''

def BN_bn2mpi():
    '''
    `BN_bn2bin(3) - format conversions <http://www.openssl.org/docs/crypto/BN_bn2bin.html>`_

    .. code-block:: c

        int BN_bn2mpi(const BIGNUM *a, unsigned char *to);



    BN_bn2mpi() と BN_mpi2bn() は

        - `BIGNUM`_ 構造体
        - ４バイトのビッグエンディアンのバイト列とその長さを表す４バイトのビッグエンディアン

    との間で書式変換する。
    
    MSB(the most significant bit:最上位ビット)は負の数を表します。
    (MSBがセットされたら、nullバイト(0x00) が先頭に付与されます )
    '''

def DN_mpi2bn():
    '''

    .. code-block:: c

        BIGNUM *BN_mpi2bn(unsigned char *s, int len, BIGNUM *ret);

    - M2Crytpoは ECDSA_sigで作成した署名を DN_bn2mpiで(r,s)のtupleに変換しています。
    '''


