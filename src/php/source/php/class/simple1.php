<?php

class Message{
  public $id;

  function dispId(){
    print("current id= $this->id .\n" );

    $this->{"hoge"} = "hogehoge";
  }
}


$m = new Message();
$m->id=1;
$m->dispId();

echo  "*** クラスの名称を使ってインスタンス作成できます\n";

$class_name = 'Message';
$m2 = new $class_name();
$m2->id=2;

echo "*** $インスタンス->{'メンバー名'}を設定すると、'\n";
echo "*** $インスタンス->メンバー名をで参照できます。";

$m2->dispId();

