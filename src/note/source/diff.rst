==========
diff
==========

-x と -q で一覧だけ出す
=============================================

- -x で .svn ディレクトリを \*.pyc を無視します。
- -q でファイル名だけを結果で出力します。
- -r でサブディレクトリに渡って検索します。

::

     1 (main)hdknr@sqg:~/ve/main/src/cms/next_milestone/website$ diff -q -x "*.pyc" -x .svn -r core ../../prev_milestone/website/core   | more
     2 ../../prev_milestone/website/coreだけに発見: fixtures
     3 ファイルcore/models.pyと../../prev_milestone/website/core/models.pyは違います
     4 ファイルcore/tests.pyと../../prev_milestone/website/core/tests.pyは違います

