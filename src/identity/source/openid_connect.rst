================
OpenID Connect
================

Based on "`Welcome to OpenID Connect <http://openid.net/wg/connect/>`_ " provided by `OpenID Foundation <http://openid.net/foundation/>`_ ..

Current Version
===============

.. glossary::


    Core
        Defines the core OpenID Connect functionality: 

        authentication built on top of :doc:`OAuth 2.0 <oauth>` 
        and the use of Claims to communicate information about the End-User

        :doc:`core.rst <core>`

    Discovery 
        (Optional) 

        Defines how Clients dynamically discover information about OpenID Provider

        :doc:`discovery.rst <discovery>`

    Dynamic Registration 
        (Optional) 

        Defines how clients dynamically register with OpenID Providers


        :doc:`reg.rst <reg>``

    Session Management 
        (Optional) 

        Defines how to manage OpenID Connect sessions, 
        including logout functionality

        :doc:`session.rst <session>`

    OAuth 2.0 Multiple Response Types 
        Defines several specific new OAuth 2.0 response types

        :doc:`oauth_responses.rst <oauth_responses>`

    OAuth 2.0 Form Post Response Mode 
        (Optional) 

        Defines how to return OAuth 2.0 Authorization Response parameters 
        (including OpenID Connect Authentication Response parameters) 
        using HTML form values that are auto-submitted by the User Agent using HTTP POST

        :doc:`oauth_posts.rst <oauth_posts>`

Below are links to the HTML versions of the released copies of the related implementer’s guides:

.. glossary::
    Basic Client Profile 
        Simple subset of the Core functionality 
        for a web-based Relying Party using the OAuth code flow

        :doc:`basic.rst <basic>`

    Implicit Client Profile 
        Simple subset of the Core functionality 
        for a web-based Relying Party using the OAuth implicit flow

        :doc:`implicit.rst <implicit>`
