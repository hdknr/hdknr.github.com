=======
Syntax
=======


表記
=====


- [pattern]   オプション(あってもなくてもよい)
- {pattern}   0回以上のくりかえし
- (pattern)   グループ化
- pat1 | pat2     選択
- pat<pat'>   差異 --- pat によって生成される要素のうちpat' によって生成される要素を除いたもの
- fibonacci   タイプライタフォントで表現された終端構文

- http://www.sampou.org/haskell/report-revised-j/exps.html

Dashes::

    dashes  ->  -- {-}


Comment::

    opencom     ->  {-
    closecom    ->  -} 


Expression :: 

    aexp        ->  qvar    (variable)
                |   gcon    (general constructor)
                |   literal

General Constructor:: 
            
    gcon        ->  ()
                |   []
                |   (,{,})
                |   qcon

Symbol::

    ascSymbol   ->  ! | # | $ | % | & | * | + | . | / | < | = | > | ? | @
                |   \ | ^ | | | - | ~ 

    uniSymbol   ->  any Unicode symbol or punctuation
    special     ->  ( | ) | , | ; | [ | ] | `| { | } 
    symbol      ->  ascSymbol | uniSymbol<special | _ | : | " | '>

Variable::

    varid                               (variables)
    var         ->  varid | ( varsym )  (variable)
    qvar        ->  qvarid | ( qvarsym )    (qualified variable)
    varsym      ->  ( symbol {symbol | :})<reservedop | dashes>

Operator:: 

    reservedop  ->  .. | : | :: | = | \ | | | <- | -> | @ | ~ | => 
    varop       ->  varsym | `varid `   (variable operator)

::

    con         ->  conid | ( consym )  (constructor)

    qcon        ->  qconid | ( gconsym )    (qualified constructor)
    qvarop      ->  qvarsym | `qvarid `     (qualified variable operator)
    conop       ->  consym | `conid `   (constructor operator)
    qconop      ->  gconsym | `qconid `     (qualified constructor operator)
    op          ->  varop | conop   (operator)
    qop         ->  qvarop | qconop     (qualified operator)
    gconsym     ->  : | qconsym




予約語
========

- :doc:`if`
- :doc:`case`


| class | data | default | deriving | do | else |  import | in | infix | infixl | infixr | instance | let | module | newtype | of | then | type | where | _ 


