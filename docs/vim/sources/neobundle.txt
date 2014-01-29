========================
NeoBundle
========================

.. contents::
    :local:

- :doc:`vundle`

Install
========

.. code-block:: bash

    vim ~/.vimrc.neobundle

.. code-block:: vim

    set nocompatible " Be iMproved
    if has('vim_starting')
    set runtimepath+=~/.vim/bundle/neobundle.vim/
    endif
    call neobundle#rc(expand('~/.vim/bundle/'))
    NeoBundleFetch 'Shougo/neobundle.vim'
    NeoBundle 'Shougo/vimproc'
    NeoBundle 'thinca/vim-ref'
    NeoBundle 'tpope/vim-surround'
    NeoBundle 'mattn/gist-vim'
    NeoBundle 'hdknr/orevim'
    NeoBundle 'tpope/vim-fugitive'
    NeoBundle 'Lokaltog/vim-easymotion'
    NeoBundle 'rstacruz/sparkup', {'rtp': 'vim/'}
    NeoBundle 'L9'
    NeoBundle 'FuzzyFinder'
    NeoBundle 'python_ifold' 
    NeoBundle 'git://git.wincent.com/command-t.git'
    NeoBundle 'http://svn.macports.org/repository/macports/contrib/mpvim/'
    NeoBundle 'https://bitbucket.org/ns9tks/vim-fuzzyfinder'
    filetype plugin indent on " Required!
    NeoBundleCheck

.. code-block:: bash

    vi ~/.vimrc

.. code-block:: vim

    source ~/bin/home/.vimrc.neobundle

.. code-block:: bash

    mkdir -p ~/.vim/bundle 
    git clone git://github.com/Shougo/neobundle.vim ~/.vim/bundle/neobundle.vim


.. code-block:: bash

    vim

.. literalinclude:: _static/neobundle/install_plugins.txt

    

