# -*- coding: utf-8 -*-
'''
.. code-block:: c

    /* openssl/ossl_typ.h  */

    typedef struct bignum_st BIGNUM;    


.. code-block:: c

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


