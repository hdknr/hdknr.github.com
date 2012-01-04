#!/bin/bash
#
pip install jinja2
pip install -e git+ssh://git@github.com/hdknr/jinjatag.git#egg=jinjatag
pip install -e hg+ssh://hg@bitbucket.org/hdknr/sphinx-dev#egg=sphinx
pip install -e hg+ssh://hg@bitbucket.org/hdknr/ve#egg=ve
#
hg clone ssh://hg@bitbucket.org/hdknr/hdknr.bitbucket.org ../hdknr.bitbucket.org
#git clone git@github.com:hdknr/hdknr.github.com.git
#
