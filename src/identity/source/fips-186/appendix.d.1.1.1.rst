D.1.1.1 Choice of Key Lengths 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
    - E  カーブ
    - G(E) ベースポイント
    - n 桁数 (大きい素数)
    - hn ポイント数 

        - h : コファクター
            hはnで割り切れないこと
            小さい数(1,2,4)

The principal parameters for elliptic curve cryptography 
are the :term:`elliptic curve` E and 
a designated point G on E called the :term:`base point`. 

The base point has order n, which is a large prime. 

The number of points on the curve is hn for some integer h (the :term:`cofactor`), 
which is not divisible by n. 

For efficiency reasons, 
it is desirable to have the cofactor be as small as possible. 

All of the curves given below have cofactors 1, 2, or 4. 

As a result, the private and public keys 
for a curve are approximately the same length.
