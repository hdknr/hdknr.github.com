<?php

$obj = (object) 'obj';

echo var_dump( $obj );

$var = 'var';
$obj->{'var'} = "a variable";
echo $obj->{'var'} == $obj->var,"\n";
echo $obj->{$var},"\n";

echo var_dump( $obj );

echo "*** unsetするとメンバーを取除くことができます。\n";
unset( $obj->var );
echo var_dump( $obj );
