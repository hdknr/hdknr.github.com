==============
rc file
==============

.. contents::
    :local:


Debianパッケージ
==============================

/usr/share/vim/vimrc
------------------------

単純に vimrc.local をロードしているだけです。

::

    runtime! debian.vim
    
    if filereadable("/etc/vim/vimrc.local")
      source /etc/vim/vimrc.local
    endif

/etc/vim/vimrc
------------------------

/usr/share/vim/vimrc と同じないようです



/etc/vim/vimrc.local
------------------------

存在していません。カスタマイズ用です。(?)

/etc/vim/vimrc.tiny
----------------------

vim-tiny パッケージ用です。

:: 

    set runtimepath=~/.vim,/var/lib/vim/addons,/usr/share/vim/vimfiles,/usr/share/vim/vim73,/usr/share/vim/vimfiles/after,/var/lib/vim/addons/after,~/.vim/after

    set compatible


ユーザー設定
=============

~/.vimrc
-----------

ユーザーのカスタマイズ用ファイル。
