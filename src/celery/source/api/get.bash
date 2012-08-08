#!/bin/bash
#http://docs.celeryproject.org/en/latest/_sources/reference/celery.txt

GREP_OPTIONS=

grep '^ *celery' index.rst | while read api ; do
    echo "[$api]";
    wget http://docs.celeryproject.org/en/latest/_sources/reference/$api.txt;
done
