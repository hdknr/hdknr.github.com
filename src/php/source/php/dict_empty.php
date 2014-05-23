<?php

// 要素の空チェックはempty, ただしリテラル''も null もempty
//
php > $a = array('a' => 1, 'b'=>'', 'c'=null,);
php > echo "a=", empty($a['a']), ",b=", empty($a['b']), ",c=", empty($a['c']), ",d=", empty($a['d']),"\n";
a=,b=1,c=1,d=1

php > echo $a['a'] == null,"\n";

php > echo $a['d'] == null,"\n";
1
php > echo $a['c'] == null,"\n";
1
php > echo $a['b'] == null,"\n";
1
