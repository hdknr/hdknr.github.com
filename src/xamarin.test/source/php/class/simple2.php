<?php

class Message{
  protected $id;

  function __construct($id) {
    $this->id = $id;
    $this->{'debug_message'} = "speified number is $id";
  }  

  function dispId(){
    print("current id= $this->id .\n" );
  }
}


$m = new Message(32);
$m->dispId();
echo $m->{'debug_message'} , "\n";
echo $m->debug_message, "\n";
echo var_dump( $m );

$m->{'subject'} = "hello PHP class";
echo $m->subject ,"\n";
echo var_dump( $m );

