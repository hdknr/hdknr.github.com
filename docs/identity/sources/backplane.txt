==========
Backplane 
==========

http://developers.janrain.com/documentation/backplane-protocol/


.. contents:: Backplane


Protocol
================

Overview
----------------

The Backplane Protocol is an open source protocol, 
developed to simplify communications between multiple web widgets 
and applications on the same web page. 

Instead of each widget or application using their own scheme to access user data, 
Backplane-enabled widgets listen to a single, 
common Backplane Server for updates.

The Backplane Protocol can publish different types of messages, 
alerting widgets when users have authenticated, 
or activities the user is sharing with social network.

Publishing Authentication Data on Backplane
------------------------------------------------

1. User is authenticated with a Backplane-enabled sign-in widget, such as Janrain Engage.
2. The widget publishes a message on a Backplane Server channel.
3. Widgets on the web page listening to the Backplane are updated.

Audiences
---------------

Two audiences:

-    Website Owners — Add Backplane functionality to a website.
-    Product Developers — Add Backplane support to a product, such as a widget.

Version
----------

The Backplane Protocol is an open source, 
cross-company initiative aimed at advancing web app technology. 
There are currently two versions:

-   Backplane Protocol 1.2 – The first public implementation of Backplane Protocol. 
    Supports publishing Identity messages.

-   Backplane Protocol 2.0 – Uses :term:`OAuth2` for the **authorization process**. 
    Supports an Identity Scenario, and will support an **Activity Streams** Scenario when implemented. 
    `Messages`_ also have been re-engineered to send only **header** information 
    to browser or anonymous clients,  
    the **payload** is sent to authenticated clients as specified in the protocol.

Protocol Flow
====================

Figure 1 shows an example of the Backplane Protocol identity message flow using Janrain as the authenticating service.

.. figure:: backplane/bpp-tech-diagram-1.png
    :scale: 70%
    
    Figure 1

[A] Message Posting with the Backplane Protocol
------------------------------------------------------------

    A1) :term:`User` signs in to website.

    A2) :term:`Identity connector` publishes Identity/Login events to the Backplane Server.

[B] Message Notification
------------------------------------------------------------

    B1) A Backplane-compliant application polls the :term:`Backplane Server` for `messages`_ .

    B2) The :term:`Backplane Server` delivers the message to the clients running in the browser, absent the payload.

    B3) The :term:`Backplane JavaScript` distributes the message to apps that are registered for the message.

[C] Message Retrieval
------------------------------------------------------------

    C1) :term:`Widgets` make :term:`JSONP` calls to their servers.

    C2) :term:`Widget Server` calls :term:`Backplane Server` for full message and payload.

    C3) :term:`Widget Server` securely receives payload.

    C4) :term:`Widget Server` returns subset of payload to application on website.

Messages
============


Messages in Backplane Protocol v1.2 versus messages in Backplane Protocol 2.0
------------------------------------------------------------------------------------------

Add to Your Website
==============================



Obtain Bus Name and Credentials from Dashboard
-------------------------------------------------------

Add backplane.js
-------------------------------------------------------

Initialize the Backplane Object
-------------------------------------------------------

Configure Backplane Channel for Engage or Capture
-------------------------------------------------------


