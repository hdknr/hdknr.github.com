=====================
リスト:List
=====================

.. contents::
    :local:

.. glossary::

    リスト
    List
        - http://www.haskell.org/ghc/docs/latest/html/libraries/base/Data-List.html

    連結
        - :ref:`list.concat`

    cons演算子
        - :ref:`list.cons`

    !!
        - :ref:`list.index` 

.. _list.about:

リストとは?
===============

- 一様なデータ構造。
- 同じ型の要素を複数格納。複数の型のリスト内の混在はだめです。
- 角括弧 ([]) 内で要素をカンマ(,)で区切って並べる(:ref:`list.syntax_sugar`)。


.. code-block:: haskell

    Prelude> let nums=[1,2,3,4]
    Prelude> nums
    [1,2,3,4]
    Prelude> :info nums
    nums :: [Integer]       -- Defined at <interactive>:20:5

.. _list.concat:

連結
----

- ++ 演算子を使います。

.. code-block:: haskell

    Prelude> [1,2,3] ++ [4,5,6]
    [1,2,3,4,5,6]
    Prelude> :info it
    it :: [Integer]         -- Defined at <interactive>:26:1V



文字列は文字のリスト
-------------------------

.. code-block:: haskell

    relude> "Haskell"
    "Haskell"
    Prelude> :info it
    it :: [Char]    -- Defined at <interactive>:28:1

- 長い文字列に繰り返し :ref:`++ <list.concat>`  を使うと時間がかかるので注意。

.. _list.cons:

cons演算子(:)
----------------

- リストの先頭に何かを追加する処理は軽くなる。
- リストの型の単一データ : リスト

.. code-block:: haskell

    Prelude> 'A':" cat"
    "A cat"
    Prelude> :info :
    data [] a = ... | a : [a]       -- Defined in `GHC.Types'
    infixr 5 :

- リストの最後に要素を追加するには ++ する

.. code-block:: haskell

    Prelude> "cat" ++ "s"
    "cats"
    Prelude> [1,2] ++ [3]
    [1,2,3]

.. _list.syntax_sugar:

構文糖衣
-------------

- [] は空のリスト

.. code-block:: haskell

    Prelude> []
    []
    Prelude> :info it
    it :: [a]       -- Defined at <interactive>:8:1

- 実際は 要素1:要素2:...:要素n:[] の構文糖衣。つまり空のリストに対する :ref:`list.cons` の繰り返し。

.. code-block:: haskell

    Prelude> 1:2:3:[]
    [1,2,3]
    Prelude> 1:2:3:[] == [1,2,3]
    True

.. code-block:: haskell

    Prelude> []
    []
    Prelude> 3:it
    [3]
    Prelude> 2:it
    [2,3]
    Prelude> 1:it
    [1,2,3]


.. _list.index:

要素へのアクセス
------------------

- 要素は "0" 番から始まる。
- !! 演算子を使う

    .. code-block:: haskell

        Prelude> "Haskell" !! 2
        's'

- 範囲外で例外

    .. code-block:: haskell

        Prelude> "Haskell" !! 7
        *** Exception: Prelude.(!!): index too large

    .. code-block:: haskell

        Prelude> "Haskell" !! (-1)
        *** Exception: Prelude.(!!): negative index
        

リスト in リスト
--------------------


- リストの中のリスト長は変わってもいいが、全ての要素は同じ型である必用があります。

    .. code-block:: haskell
    
        Prelude> [ [1,2],[3,4,5],[6,7,8,9],[10,11,12]]
        [[1,2],[3,4,5],[6,7,8,9],[10,11,12]]
        
        Prelude> [ [1,2],[3,4,5],[6,7,8,9],[10,[11,12]]]
        
        <interactive>:12:4:
            No instance for (Num [t0])
              arising from the literal `1`
            Possible fix: add an instance declaration for (Num [t0])
            In the expression: 1
            In the expression: [1, 2]
            In the expression:
              [[1, 2], [3, 4, 5], [6, 7, 8, ....], [10, [11, 12]]]


リスト比較
--------------------

- 要素の型が比較可能であれば、リストも比較可能。
- <,<=,>=,> 


.. code-block:: haskell

    Prelude> [1,2] < [1,3]
    True

    Prelude> [1,2] > [1,3]
    False

    Prelude> [1,2] == [1,2]
    True

    Prelude> [1,2] > [1,2,3]
    False

    Prelude> [1,2] < [1,2,3]
    True


操作関数
===========


部分
-----

.. code-block:: haskell


    Prelude> head [1,2,3,4]
    1
    Prelude> tail [1,2,3,4]
    [2,3,4]
    Prelude> last [1,2,3,4]
    4
    Prelude> init [1,2,3,4]
    [1,2,3]
    Prelude> take 2 [1,2,3,4]
    [1,2]
    Prelude> drop 2 [1,2,3,4]
    [3,4]

.. code-block:: python

    >>> [1,2,3,4][0]
    1
    >>> [1,2,3,4][1:]
    [2, 3, 4]
    >>> [1,2,3,4][-1:][0]
    4
    >>> [1,2,3,4][:-1]
    [1, 2, 3]
    >>> [1,2,3,4][:2]
    [1, 2]
    >>> [1,2,3,4][2:]
    [3, 4]


head
^^^^^^

- 先頭

tail
^^^^^^

- 先頭をのぞいた全て

last
^^^^^^

- 最後

init
^^^^^^

- 最後をのぞいた先頭を返す


.. _list.take::

take
^^^^^

- 先頭から指定された数の要素を取り出したリスト

.. code-block:: haskell

    Prelude> take (-1) [1,2,3,4]
    []

    Prelude> take 100 [1,2,3,4]
    [1,2,3,4]

drop
^^^^^^

- 指定された数の要素を先頭から落とす

.. code-block:: haskell

    Prelude> drop 100 [1,2,3,4]
    []
    Prelude> drop (-1) [1,2,3,4]
    [1,2,3,4] 

length
--------

.. code-block:: haskell

    Prelude> length [1,2,3,4]
    4


.. code-block:: python

    >>> len([1,2,3,4])
    4


null
--------

- からリストのチェック

.. code-block:: haskell

    Prelude> null []
    True
    Prelude> null [1,2,3,4]
    False


reverse
--------

.. code-block:: haskell

    Prelude> reverse [1,2,3,4]
    [4,3,2,1]

.. code-block:: python

    >>> [ a for a in reversed([1,2,3,4])]
    [4, 3, 2, 1]


- http://www.codecodex.com/wiki/Reverse_characters_in_a_string

最大/最小
----------

maximum
^^^^^^^^^

.. code-block:: haskell


    Prelude> maximum [1,2,3,4]
    4


.. code-block:: python

    >>> max([1,2,3,4])
    4

minimum
^^^^^^^^^

sum
----

- http://www.codecodex.com/wiki/Calculate_the_sum_over_a_container

.. code-block:: haskell

    Prelude> sum [1,2,3,4]
    10

.. code-block:: python

    >>> sum([1,2,3,4])
    10


elem
-----

.. code-block:: haskell

    Prelude> elem 4 [1,2,3,4]
    True

.. code-block:: python

    >>> 4 in [1,2,3,4]
    True

.. _list.range:

レンジ(range)
===============

単純なレンジ
-------------

.. code-block:: haskell

    Prelude> [1..10]
    [1,2,3,4,5,6,7,8,9,10]
    Prelude> ['a'..'z']
    "abcdefghijklmnopqrstuvwxyz"

- Fromから始めて、Fromの値がToより大きくなるまで列挙する。
- よって From > To だと空 

    .. code-block:: haskell

        Prelude> [10..1]
        []

- From == To だと １件

    .. code-block:: haskell

        Prelude> [10..10]
        [10]

ステップ
----------

- [init,from..to] : initから始めて、from-initのステップごとにtoまで

.. code-block:: haskell

    Prelude> [2,4..11]
    [2,4,6,8,10]

    Prelude> [2,5..10]
    [2,5,8]

    Prelude> [2,6..10]
    [2,6,10]

減少列:

.. code-block:: haskell

    Prelude> [10,9..1]
    [10,9,8,7,6,5,4,3,2,1]

無限リスト
=============

- :term:`遅延評価` なので、無限リストというものがありえる。つまり評価を続ける限り続くし、やめたら終わり。

    - 定義するだけだと問題なし

        .. code-block:: haskell

            Prelude> let a = [0,0..]

    - 評価すると無限ループ

        .. code-block:: haskell

            Prelude> a
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,........
            ....
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,^CInterrupted.

- :ref:`list.take`  を使って無限リストから有限の数を取り出す

    .. code-block:: haskell
        
        Prelude> let n = 10 :: Int
        Prelude> take n [0,0..]
        [0,0,0,0,0,0,0,0,0,0]

浮動小数点
--------------

.. code-block:: haskell

    Prelude> [0.1,0.3..1]
    [0.1,0.3,0.5,0.7,0.8999999999999999,1.0999999999999999]


.. _list.cycle:
    
cycle
-------

.. code-block:: haskell

    Prelude> take 10 $ cycle [1,2,3]
    [1,2,3,1,2,3,1,2,3,1]
    
.. _list.repeat:
    
repeat
-------

.. code-block:: haskell

    Prelude> take 10 $ repeat 5
    [5,5,5,5,5,5,5,5,5,5]

    Prelude> take 10 $ repeat [1,2,3]
    [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

.. _list.replicate:
    
replicate
---------------------

.. code-block:: haskell

    Prelude> replicate 3 4
    [4,4,4]

    Prelude> replicate 3 [1,2,3]
    [[1,2,3],[1,2,3],[1,2,3]]
