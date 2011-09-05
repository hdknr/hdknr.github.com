Landslide
===============================

About
-----

- Original  https://github.com/adamzap/landslide
- Fork      https://github.com/hdknr/landslide

----

Merginging from Other's remote
---------------------------------------

Adding remote ::

    $ git remote add godfat https://github.com/godfat/landslide.git

Pull a specific branch::

    $ git pull godfat embed-image-in-header

Push to my master ::

    $ git push

---- 

Ex. Adding remote ::

    (main)hdknr@sqg:~/ve/main/src/landslide$ git remote add godfat https://github.com/godfat/landslide.git
    (main)hdknr@sqg:~/ve/main/src/landslide$ git config -l
    user.name=hdknr
    user.email=gmail@hdknr.com
    core.repositoryformatversion=0
    core.filemode=true
    core.bare=false
    core.logallrefupdates=true
    remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
    remote.origin.url=git://github.com/hdknr/landslide.git
    branch.master.remote=origin
    branch.master.merge=refs/heads/master
    remote.godfat.url=https://github.com/godfat/landslide.git
    remote.godfat.fetch=+refs/heads/*:refs/remotes/godfat/*


---- 

Ex. Pull a specific branch ::

    (main)hdknr@sqg:~/ve/main/src/landslide$ git pull godfat embed-image-in-header
    
    From https://github.com/godfat/landslide
     * branch            embed-image-in-header -> FETCH_HEAD
    Merge made by recursive.
     src/landslide/generator.py |    3 +++
     1 files changed, 3 insertions(+), 0 deletions(-)

---- 

Ex. Push to my master ::

    (main)hdknr@sqg:~/ve/main/src/landslide$ git push
    
    Counting objects: 10, done.
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (4/4), 419 bytes, done.
    Total 4 (delta 2), reused 0 (delta 0)
    To ssh://git@github.com/hdknr/landslide.git
    ab9d026..06f9fd3  master -> master

----

Install by PIP
===============

pip ::

    $ pip install -e git+ssh://git@github.com/hdknr/landslide.git#egg=landslide

