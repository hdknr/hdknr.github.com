===================================================
リスト内包:List Comprehension
===================================================


.. contents::
    :local:

.. glossary::

    リスト内包
    リスト内包表記
    List Comprehension
        - http://en.wikipedia.org/wiki/List_comprehension
        - http://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension)

サンプル
==========


定義
=====
    
- http://www.cs.arizona.edu/~collberg/Teaching/372/2005/Html/Html-13/index.html

::

    [ expr| qualifier, qualifier,...]

- "Generate a list where the elements are of the form *expr*, such that the elements fulfill the conditions in the *qualifiers*."

    - *expr* (Haskellの表現) の形の要素を含むリストを生成します。 この要素は *qualifiers* にある条件を満たす必用があります。 

- Qualifiers (述語)

    1. Generator
    2. Filter
    3. Local Definitions 

Generator Qualifiers
---------------------------------

::

    ジェネレートされる変数 <-  リスト

.. code-block:: haskell

    Prelude> [ x * 2 | x <- [1..10] ]
    [2,4,6,8,10,12,14,16,18,20]


.. code-block:: python

    >>> [ i * 2 for i in range(1,11)]
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



Filter Qualifiers
---------------------------------

- ジェネレータをフィルターする表現

.. code-block:: haskell

    Prelude> [ x * 2 | x <- [1..10], x * 2 < 10 ]
    [2,4,6,8]

.. code-block:: python

    >>> [ i * 2 for i in range(1,11) if i*2 < 10]
    [2, 4, 6, 8]


Local Difinition
--------------------

.. code-block:: haskell

    Prelude> [ x * y | x <- [1..10], let y = 3]
    [3,6,9,12,15,18,21,24,27,30]


.. note::

    Python は出来ないかも。


応用
-------

.. code-block:: haskell

    Prelude> [ (x * z,[y,v]) | x <- [1..10],  y <- ['a'..'c'], let z = 3, let v ='*', x * z `mod` 2 == 0, x*z > 10]
    [(12,"a*"),(12,"b*"),(12,"c*"),(18,"a*"),(18,"b*"),(18,"c*"),(24,"a*"),(24,"b*"),(24,"c*"),(30,"a*"),(30,"b*"),(30,"c*")]


.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude|   dPos :: [Int] -> [Int]
    Prelude|   dPos xs = [ 2*x | x <-xs, x>0]
    Prelude| :}
    Prelude> dPos [-1,-2,1,2,3]
    [2,4,6]


.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude|   spc :: Int -> String
    Prelude|   spc n = [' ' | i <- [1..n]]
    Prelude| :}
    Prelude> spc 10
    "          "

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude|   factors :: Int -> [Int]
    Prelude|   factors n = [ i | i <- [2..n-1], n `mod` i == 0 ]
    Prelude| :}
    Prelude> factors 100
    [2,4,5,10,20,25,50]
    Prelude> factors 5
    []
    Prelude> factors 6
    [2,3]


traids : x^2 + y^2 = z^2 , x,y,z < n

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| triads n = [ (x,y,z) |
    Prelude|    x <- [1..n], y <- [1..n], z <- [1..n],
    Prelude|    x^2  + y^2 == z^2 
    Prelude|    ]
    Prelude| :}
    Prelude> triads 5
    [(3,4,5),(4,3,5)]

improved traids: 重なりを避ける

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude| triads n = [ (x,y,z) |
    Prelude|    x <- [1..n], y <- [x..n], z <- [y..n],
    Prelude|    x^2 + y^2 == z^2
    Prelude|    ]
    Prelude| :}
    Prelude> triads 11
    [(3,4,5),(6,8,10)]

応用:指定した金額に足りる小銭の数
------------------------------------

change.hs:

.. code-block:: haskell

    type Coin = Int

    coins :: [Coin]
    coins = reverse [1,5,10,50,100,500] 
    
    change amount = head( all_change amount )
    
    all_change :: Int -> [[Coin]]
    all_change 0 = [[]]
    all_change amount = [ c:cs |
        c <- coins, amount >= c,
        cs <- all_change (amount - c) 
        ] 

.. code-block:: haskell
    
    Main> :l change.hs

    Main> change 598
    [500,50,10,10,10,10,5,1,1,1]

    Main> all_change 12
    [[10,1,1],[5,5,1,1],[5,1,5,1],[5,1,1,5],
    [5,1,1,1,1,1,1,1],[1,10,1],[1,5,5,1],[1,5,1,5],
    [1,5,1,1,1,1,1,1],[1,1,10],[1,1,5,5],
    [1,1,5,1,1,1,1,1],[1,1,1,5,1,1,1,1],[1,1,1,1,5,1,1,1],
    [1,1,1,1,1,5,1,1],[1,1,1,1,1,1,5,1],[1,1,1,1,1,1,1,5],
    [1,1,1,1,1,1,1,1,1,1,1,1]]

