===========
Homebrew
===========

.. contents::
    :local:

Python
=======

- `PIL のインストールは注意 <http://note.harajuku-tech.org/homebrew-pil-seqdiag>`_


ローカル変更後のupdate
================================================

.. code-block:: bash

    (docs)Peeko:celery hide$ brew update
    
    error: Your local changes to the following files would be overwritten by merge:
            Library/Formula/netpbm.rb
    Please, commit your changes or stash them before you can merge.
    Aborting
    Error: Failure while executing: git pull -q origin refs/heads/master:refs/remotes/origin/master

.. code-block:: bash

    (docs)Peeko:sphinx hide$ cd /usr/local/Library/Formula/

.. code-block:: bash

    (docs)Peeko:Formula hide$ git status | more

    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       new file:   ../Aliases/gperftools
    #       new file:   ../Contributions/cmds/brew-aspell-dictionaries
    #       modified:   ../Contributions/cmds/brew-leaves.rb

.. code-block:: bash

    (docs)Peeko:Formula hide$ git commit -a -m "Update latest"
    
    [master 70382c7] Update latest
     1602 files changed, 9206 insertions(+), 5881 deletions(-)
     create mode 120000 Library/Aliases/gperftools
     create mode 100755 Library/Contributions/cmds/brew-aspell-dictionaries
     create mode 100755 Library/Contributions/cmds/brew-md5-to-sha1
     ....
    
.. code-block:: bash

    (docs)Peeko:Formula hide$ git commit -a -m "merge"
    [master eb5433e] merge
    
.. code-block:: bash

    (docs)Peeko:Formula hide$ brew update                                                                                                                                             
    Already up-to-date.
    
