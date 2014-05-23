<?php


php > $a = array('a' => 1);
php > echo var_dump($a);
array(1) {
  ["a"]=>
  int(1)
}

php > $b = array('b' => 2) ;
php > echo var_dump($b);
array(1) {
  ["b"]=>
  int(2)
}

php > $c = $a + $b;

php > echo var_dump($c);
array(2) {
  ["a"]=>
  int(1)
  ["b"]=>
  int(2)
}

