<?php

// 連結

php > $b = array('b' => 2 );
php > $c = array('c' => 3 );
php > $a = array('a' => 1 );
php > $d = $a + $b + $c;
php > var_dump($d);
array(3) {
  ["a"]=>
  int(1)
  ["b"]=>
  int(2)
  ["c"]=>
  int(3)
}


// 上書きされない

php > $a2 = array('a' => '20');
php > $a3 = array('a' => '30');

php > $d = $a + $a2 + $a3;
php > var_dump($d);
array(1) {
  ["a"]=>
  int(1)
}
php > $d = $a3 + $a2 + $a;
php > var_dump($d);
array(1) {
  ["a"]=>
  string(2) "30"
}


