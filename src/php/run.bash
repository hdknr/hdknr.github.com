#!/bin/bash

SRC=source/php

runphp()
{
    php $1 > $1.log
}

export -f runphp

find $SRC -name "*.php"  -exec bash -c 'runphp {}' \;
