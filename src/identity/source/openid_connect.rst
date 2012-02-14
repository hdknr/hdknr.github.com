================
OpenID Connect
================

Based on "`Welcome to OpenID Connect <http://openid.net/connect/>`_ " provided by `OpenID Foundation <http://openid.net/foundation/>`_ ..

Current Version
===============

.. glossary::

    Basic
        :doc:`basic` -  Light-weight simple no-frills version for a simple Relying Party.

    Standard
        :doc:`standard` - Full version of a HTTP binding. References :term:`Messages`.

    Messages
        :doc:`messages` - Lists all the messages that are used in OpenID Connect. 
        You can use this to create a new Bindings of the Connect, such as OpenID Connect for XMPP.
        - Checked Draft 07, December 22, 2011 

    Registration
        :doc:`reg` - (Optional) Defines how clients register with OpenID Providers.

    Discovery
        :doc:`discovery` - (Optional) Defines how user and server endpoints are discovered.
        - Checkd Draft 07 , Dec 22, 2011

    Session
        :doc:`session` - (Optional) Defines how to manage sessions for OpenID Connect.


.. note::

    Nat's `anncounce on ML <http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20111219/001377.html>`_ about the approval of the Implementer's Draft

    ::

        The OpenID AB+Connect Working Group recommends approval of the
        following specifications as OpenID Implementer’s Drafts:
        
        •       Basic Client Profile – Simple self-contained specification for
        a web-based Relying Party.  (This spec contains a subset of the
        information in Messages and Standard.)
        •       Discovery – Defines how user and provider endpoints can be
        dynamically discovered.
        •       Dynamic Registration – Defines how clients can dynamically
        register with OpenID Providers.
        •       Messages – Defines all the messages that are used in OpenID
        Connect.  (These messages are used by the Standard binding.)
        •       Standard – Complete HTTP binding of the Messages, for both
        Relying Parties and OpenID Providers.
        •       Multiple Response Type Encoding – Registers OAuth 2.0
        response_type values used by OpenID Connect.
        An Implementer’s Draft is a stable version of a specification
        providing intellectual property protections to implementers of the
        specification.  This note starts the 45 days public review period for
        the specification drafts in accordance with the OpenID Foundation IPR
        policies and procedures.  This review period will end on Monday,
        February 6, 2012.Unless issues are identified during the review that
        the working group believes must be addressed by revising the drafts,
        this review period will be followed by a seven day voting period
        during which OpenID Foundation members will vote on whether to approve
        these drafts as OpenID Implementer’s Drafts. The specifications are
        posted at these locations:•
        http://openid.net/specs/openid-connect-basic-1_0-15.html
        •       http://openid.net/specs/openid-connect-discovery-1_0-07.html
        •       http://openid.net/specs/openid-connect-registration-1_0-08.html
        •       http://openid.net/specs/openid-connect-messages-1_0-07.html
        •       http://openid.net/specs/openid-connect-standard-1_0-07.html
        •       http://openid.net/specs/oauth-v2-multiple-response-types-1_0-03.html
         A description of OpenID Connect can be found at
        http://openid.net/connect/. The working group page is
        http://openid.net/wg/connect/. Information on joining the OpenID
        Foundation can be found at
        https://openid.net/foundation/members/registration.  Foundation
        members will be asked to vote on approving these specifications as
        Implementer’s Drafts. You can send feedback on the specifications in a
        way that enables the working group to act on your feedback by (1)
        signing the contribution agreement at
        http://openid.net/intellectual-property/ to join the AB+Connect
        working group, (2) joining the working group mailing list at
        http://lists.openid.net/mailman/listinfo/openid-specs-ab, and (3)
        sending your feedback on that list.
        -- 
        Nat Sakimura (=nat)
        Chairman, OpenID Foundation
        http://nat.sakimura.org/
        @_nat_en

