#!/bin/bash

# 全ての引数
echo $@

# ループ
for a in $@; do
    echo "ARG",$a;
done
