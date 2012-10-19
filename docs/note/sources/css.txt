=====
CSS
=====

.. contents:: CSS

@import
========

.. code-block:: css

    @import "hoge.css";

とか
    
.. code-block:: css

    @import url("basic.css");


<textarea>
============

行の高さ(line-height)
------------------------------------

::

    line-height : 150%;         // 文字高さ1.5倍
    line-height : 1.5 ;         // 文字高さ1.5倍
    line-height : 1.5em ;       // 文字高さ1.5倍
    

幅(width)
----------

cols属性をオーバーライドします。

高さ(height)
----------------

rows属性をオーバーライドします。


CSS Reset 
============

.. glossary::
    
    CSS Reset
    Reset CSS
        - 一貫性のある基準(baseline)に対してHTMLのスタイルをリセットする為の圧縮されたCSS
        - 例えば全てのブラウザはそれぞれのデフォルトの「ユーザーエージェント」スタイルシートを保っています。
 
        - http://www.cssreset.com/what-is-a-css-reset/
        - http://www.cssreset.com/
        - http://www.cssreset.com/css-tutorials/

- `どのReset CSS使うべきか? <http://note.harajuku-tech.org/which-css-reset-should-i-use-css-reset>`_ 
- `コツ <http://note.harajuku-tech.org/which-css-reset-should-i-use-css-reset-65974>`_

