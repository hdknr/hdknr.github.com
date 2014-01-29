=============
インストール
=============

.. contents::
    :local:


MySQL
===========

Ubuntu/Debian

.. code-block:: bash

    $ sudo apt-get install php5-mysql mysql-server mysql-client

Apache
========


.. code-block:: bash

    $ sudo aptitude install apache2 libapache2-mod-php5


CentOS

    .. code-block:: bash

        $ sudo yum groupinstall "Web Server"

というか、

    .. code-block:: bash

        $ sudo yum groupinstall "Web Server" "MySQL Database client" "MySQL Database server" "PHP Support" -y

mod_macro
-----------

.. code-block::

    $ sudo aptitude install libapache2-mod-macro
