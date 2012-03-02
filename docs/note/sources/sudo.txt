======
sudo
======


sudo su - を禁止
==================

:: 

    Cmnd_Alias SHELLS = /bin/sh, /bin/csh, /bin/tcsh, /bin/bash, /usr/local/bin/bash
    Cmnd_Alias SHELLS_NONINTERACTIVE = /bin/sh -c *, /bin/csh -c *, \
    /bin/tcsh -c *, /usr/local/bin/bash -c *
    !SHELLS, SHELLS_NONINTERACTIVE,

