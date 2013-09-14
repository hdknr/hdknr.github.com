<?php

$array = array(
    "foo" => "bar",
    "bar" => "foo",
);
$array['hoge'] = 'hogehoge';

foreach($array as $key => $value )
{
  echo  "$key =>  $value\n";
}
