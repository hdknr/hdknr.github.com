#!/bin/bash

touch source/$1.rst ;make html 2>&1 | grep term | awk -F: '{ print $5}' | sort | uniq | sed -e "s/^\s\+//"
