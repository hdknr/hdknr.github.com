Breaking change in OAuth 2.0 rev. 23
===============================================================


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001672.html
-------------------------------------------------------------------------------------

I only noticed now that rev 23 had a breaking change. 
it seems to doesn't allow the response_type=code token 
unless we define another client type such as "**hybrid**".

This is a breaking change.

I wonder why I did not notice it till now.

See below.

>From :ref:`section 2.1 <oauth_2_1>` of
http://tools.ietf.org/rfcdiff?difftype=--hwdiff&url2=draft-ietf-oauth-v2-23.txt

"A client application consisting of multiple components, each with its
own client type (e.g. a distributed client with both a confidential
server-based component and a public browser-based component), *MUST*
register each component separately as a different client to ensure
proper handling by the authorization server."

Discuss.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001673.html
----------------------------------------------------------------------------------------------------

Yes I didn't see any discussion on that before the change.

It is unclear if you can define a new client type,  
it is not a real parameter.

Perhaps it is enough to say 
that any client asking for code token is hybrid 
and needs to be treated appropriately.  
Though that section seems to make having a separate client_id 
for each component mandatory.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001674.html
------------------------------------------------------------------------------------


Yes I didn't see any discussion on that before the change.

It is unclear if you can define a new client type,  
it is not a real parameter.

Perhaps it is enough to say that 
any client asking for :term:`code token` is **hybrid** 
and needs to be treated appropriately.  
Though that section seems to make
having a separate client_id for each component mandatory.

Indeed, and that's the breaking point.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001675.html
----------------------------------------------------------------------------------------------------

The way I read it, ":term:`code token`" is its own type, 
and it needs to be treated differently from either "code" or "token", 
which isn't a change. 
What the intent of the text is, I believe, 
is to keep people from using the same client id with "code" as with "token". 
This would effectively be mixing public and private clients 
in the most normal use cases, 
which is the section that it's in, 
and that's not a good thing.

I don't think it's actually a breaking change, 
but I'm less convinced of the utility of normative language here.

 -- Justin


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001676.html
----------------------------------------------------------------------------------------------------

    The way I read it, "code token" is its own type, and it needs to be treated


My first take was that but the text goes:

    a distributed client with both a confidential
    server-based component and a public browser-based component), *MUST*
    register each component separately as a different client

so looks to me that it does not allow that interpretation...


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001684.html
----------------------------------------------------------------------------------------------------

A related question came up on the OAuth WG list:
http://www.ietf.org/mail-archive/web/oauth/current/msg08548.html
though I don't know if that provides much guidance.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001677.html
----------------------------------------------------------------------------------------------------

This is the only discussion about this change.
http://www.ietf.org/mail-archive/web/oauth/current/msg08271.html

And this is the response I got in OAuth ML.
http://www.ietf.org/mail-archive/web/oauth/current/msg08548.html

According to the Eran's reply, I thought extensions (eg. response_type=code token) can overwrite the requirement.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001678.html
----------------------------------------------------------------------------------------------------

**The problem is the normative MUST language**. 
If it were SHOULD, it is less of the problem.

Since it is a MUST, we cannot extend it. 
That is the problem that I am pointing  out.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001679.html
----------------------------------------------------------------------------------------------------

Not true -- extensions can override MUST requirements 
if they specify the conditions that break it.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001682.html
----------------------------------------------------------------------------------------------------

Good to know it. 
I thought an extension could only extend 
from an extension point 
but could not override a normative  language. 
If it can, it would not be a problem.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001685.html
----------------------------------------------------------------------------------------------------

I am quite confused with this change.

In particular, 
I am not sure **response_type** is anymore relevant. 
Can't it be inferred from the client, 
since each client is bound to a security context?

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001686.html
----------------------------------------------------------------------------------------------------

If we're concerned about this change, 
we should begin discussing it on the OAuth mailing list 
and lobbying to have it undone.  
Discussing it on the AB list won't accomplish this.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001687.html
----------------------------------------------------------------------------------------------------

I agree and I am planning to raise the issue here. 
However, I would like to register it here 
that I don't think the current approach to defer 
to extensions is necessarily sufficient to remove all cause for concern by this WG.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001688.html
----------------------------------------------------------------------------------------------------

> If we’re concerned about this change, we should begin discussing it on the
> OAuth mailing list and lobbying to have it undone.  Discussing it on the AB
> list won’t accomplish this.

I just sent a message to the OAuth list in this regard. Yes, I think
this should be debated there.

Marius

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001689.html
----------------------------------------------------------------------------------------------------

So it was my attempt to see if it were a problem that we can solve
here or not and good to hear that you filed it to the oauth list.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001680.html
----------------------------------------------------------------------------------------------------

The change does not preclude these being the same physical client

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120312/001681.html
----------------------------------------------------------------------------------------------------

Right, this, too. A client could effectively have two personae.




