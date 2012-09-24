========
JSON
========

.. contents:: JSON


JSON.NET
===========

Install
---------

`NuGet <http://note.harajuku-tech.org/jsonnet-96303>`_ ::

    PM> Install-Package Newtonsoft.Json 

ソースコード::

    $ git clone https://github.com/JamesNK/Newtonsoft.Json.git


RFC4627
=============

- "The application/json Media Type for JavaScript Object Notation (JSON)"(:rfc:`4627`)

2.5. Strings
================================================

The representation of strings is similar to conventions used in the C
family of programming languages.  
A string begins and ends with quotation marks.  
All Unicode characters may be placed within the quotation marks 
except for the characters that must be escaped: 
quotation mark, reverse solidus, and the control characters (U+0000 through U+001F).

文字列の表現はC言語のファミリープログラミング言語で使われているのと同様です。
文字列はクオーテーションマーク(")で始まり、終わります。
全てのUnicode文字はクォーテーションマークの中に置くことができますが、
中にはエスケープしなければ行けない文字があります:
クォーテーションマーク, リバースソリダス(バックスラッシュ)、(U+0000からU+001Fまでの)
制御文字です。

Any character may be escaped.  
If the character is in the Basic Multilingual Plane (U+0000 through U+FFFF), 
then it may be represented as a six-character sequence: 
a reverse solidus, followed by the lowercase letter u, 
followed by four hexadecimal digits that encode the character's code point.  
The hexadecimal letters A though F can be upper or lowercase.  
So, for example, 
a string containing only a single reverse solidus character may be represented as "\\u005C".

.. _unicode_bmp: http://ja.wikipedia.org/wiki/%E5%9F%BA%E6%9C%AC%E5%A4%9A%E8%A8%80%E8%AA%9E%E9%9D%A2

全ての文字はエスケープ可能です。
`基本多面言語(BMP)(U+0000からU+FFFFまで） <unicode_bmp>`_  にある文字であれば６文字シーケンスで
表現することが可能です:
リバースソリダス, 英子文字のuそして文字のコードポイントをエンコードする４つの16進数文字が続きます。
16審のAからFは英大文字でも小文字でもいいです
なので、例えば、１個のリバースソリダス文字は "\\u005C"で表現できます。


Alternatively, 
there are two-character sequence escape representations of some popular characters.  
So, for example, 
a string containing only a single reverse solidus character may be represented more compactly as "\\\\".

逆に、よく使われる文字で２文字続きのエスケープ表現もあります。
例えば、１つのリバースソリダス文字を含んだ文字列はよりコンパクトな"\\\\"で表現することができます。

To escape an extended character that is not in the Basic Multilingual Plane, 
the character is represented as a twelve-character sequence,
encoding the UTF-16 surrogate pair.  
So, for example, 
a string containing only the G clef character (U+1D11E) may be represented as "\\uD834\\uDD1E".

`基本多面言語 <unicode_bmp>`_ に無い拡張文字をエスケープするには、
UTF-16サロゲートペアをエンコードする12文字のシーケンスで表現されます。
例えば、ト音記号(G clef character)(U+1D11E)の１文字は "\\uD834\\uDD1E" で表現されます。


::

         string = quotation-mark *char quotation-mark

         char = unescaped /
                escape (
                    %x22 /          ; "    quotation mark  U+0022
                    %x5C /          ; \    reverse solidus U+005C
                    %x2F /          ; /    solidus         U+002F
                    %x62 /          ; b    backspace       U+0008
                    %x66 /          ; f    form feed       U+000C
                    %x6E /          ; n    line feed       U+000A
                    %x72 /          ; r    carriage return U+000D
                    %x74 /          ; t    tab             U+0009
                    %x75 4HEXDIG )  ; uXXXX                U+XXXX

         escape = %x5C              ; \

         quotation-mark = %x22      ; "

         unescaped = %x20-21 / %x23-5B / %x5D-10FFFF


