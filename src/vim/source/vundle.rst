========
Vundle
========

Install
========

Vundle Checkout

::

    $ cd $HOME;  mkdir .vim ; cd .vim ; git clone git://github.com/gmarik/vundle.git

.vimで設定

::

    "-----  Vundle 
    set rtp+=~/.vim/vundle/
    call vundle#rc()
    
    Bundle 'thinca/vim-ref'
    Bundle 'tpope/vim-surround'
    Bundle 'mattn/gist-vim'
    Bundle 'hdknr/orevim'
    "Bundle 'Shougo/neocomplcache'
    "Bundle 'Shogo/unite.vim'
    "Bundle 'scrooloose/nerdcommenter'
    "Bundle 'thinca/vim-puickrun'
    "Bundle 'kana/vim-fakeclip'
    "------

.vim 確認

.. code-block:: bash

    hdknr@Blue:~$ tree .vim
    .vim
    └── vundle
        ├── autoload
        │   ├── vundle
        │   │   ├── config.vim
        │   │   ├── installer.vim
        │   │   └── scripts.vim
        │   └── vundle.vim
        ├── doc
        │   └── vundle.txt
        ├── LICENSE-MIT.txt
        ├── README.md
        └── test
            ├── minirc.vim
            └── vimrc
    
    5 directories, 9 files

vimを起動してBundleInstall

::

    :BundleInstall


Reource
========

- `Mac Homebrewでの Vundle <http://note.harajuku-tech.org/vim-vundle>`_
-
