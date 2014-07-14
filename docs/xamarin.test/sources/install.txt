=============
インストール
=============

.. contents::
    :local:


Debian
========

.. code-block:: bash

    debian$  sudo aptitude install apache2 -y
    debian$  sudo aptitude install php5 php5-cli php5-common php5-curl php5-mysql php5-xmlrpc php-pear -y
    debian$  sudo aptitude install php5-gd -y
    debian$  sudo aptitude install php5-xcache php5-cgi -y

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
