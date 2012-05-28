# -*- coding: utf-8 -*-


def dh_generate_parameters(prime_len, generator, callback,callback_arg):
    ''' generate Diffie-Hellman parameters 
        
        :param prime_len: 素数(prime)ビット長 (素数は十分大きい物を使う )
        :param generator: 小さな整数 ( 通常は 2とか5 )
        :param callback: None だと bn_generate_prime() がよばれる。  
                         ( 指定されたビット数の疑似ランダム素数がかえされる )
                         Noneじゃないと callback(3,0,callback_arg) が呼ばれる。
        :param callback_arg:
        
        - http://www.openssl.org/docs/crypto/DH_generate_parameters.html

    >>>
    >>>
    '''

def dh_check(dh, codes):
    ''' check Diffie-Hellman parameters 

        :param dh: DH structure
        :param codes: (TBD)

        - http://www.openssl.org/docs/crypto/DH_generate_parameters.html

    .. code-block:: c

        struct DH
        {
        BIGNUM *p;              // prime number (shared)
        BIGNUM *g;              // generator of Z_p (shared)
        BIGNUM *priv_key;       // private DH value x
        BIGNUM *pub_key;        // public DH value g^x
        // ...
        };
        
    '''

def ecdsa_sign( type,dgst):
    ''' ECDSA_sign_ex のラッパー。kinv= NULL,rp=NUL

        :param type: タイプ
        :param dgst: ダイジェスト
        :return: ECDSA_SIG構造体


        - http://www.openssl.org/docs/crypto/ecdsa.html

    .. code-block:: c

         struct
         {
            BIGNUM *r;
            BIGNUM *s;
         } ECDSA_SIG;

    .. code-block:: c

        /* openssl/ossl_typ.h  */

        typedef struct bignum_st BIGNUM;

        /* openssl/bn.h */

        #define BN_ULONG    unsigned long                   //  8byte
        struct bignum_st        
        {   
            BN_ULONG *d;    /* Pointer to an array of 'BN_BITS2' bit chunks. */
            int top;        /* Index of last used d +1. */

            /* The next are internal book keeping for bn_expand. */
            int dmax;   /* Size of the d array. */
            int neg;    /* one if the number is negative */
            int flags;
        };
    
    '''      
