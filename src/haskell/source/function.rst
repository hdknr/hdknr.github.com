======
関数
======

.. contents::
    :local:

パターンマッチ
===============


asパターン
================

- 値をパターンに分解する
- 同時に、パターンマッチの対象の値も参照したい


ガード
========

- 引数の対がパターンを満たした上で、性質で場合分けする時にガードを使う

.. code-block:: haskell

    Prelude> :{
    Prelude| let
    Prelude|   hoge :: Int -> String
    Prelude|   hoge n
    Prelude|     | n == 1 = "あああ"
    Prelude|     | n == 2 = "いいい"
    Prelude|     | n >  2 = "ううう"
    Prelude|     | otherwise = "?"
    Prelude| :}

    Prelude> hoge 1
    "\12354\12354\12354"
    Prelude> print $ hoge 1
    "\12354\12354\12354"
    Prelude> print $ hoge 1
    "\12354\12354\12354"
    Prelude> print $ hoge 2
    "\12356\12356\12356"
    Prelude> print $ hoge 3
    "\12358\12358\12358"
    Prelude> print $ hoge 4
    "\12358\12358\12358"
    Prelude> print $ hoge 0
    "?"V

where
=======

let
====

case
======
