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

echo "*** valueだけを指定すると、自動的に0から始まる整数がkeyになります\n";
$array = array(
    "mon","tue","wed","thr","fri","sat","sun"
);
foreach($array as $key => $value )
{
  echo  "$key =>  $value\n";
}
