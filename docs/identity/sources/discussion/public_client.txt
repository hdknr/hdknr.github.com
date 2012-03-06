Does Connect support public clients?
==============================================================

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001592.html
--------------------------------------------------------------------------------------------------

Hi all,

I'm unable to find out whether OpenID Connect supports :term:`public clients`. 
It seems Connect assumes all clients register with the OP and obtain a 
client credential. If this observation is correct, what is the reason 
for being **more restrictive** than OAuth?

regards,
Torsten.

Torsten,

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001598.html
----------------------------------------------------------------------------------------------------

From your tickets it looks like you are thinking that the :term:`Basic client profile` is for :term:`JS clients` 
in the browser doing :term:`canvas type Aps` and directly accessing the :term:`check_id` and :term:`user_info` endpoints.

The idea for what i't worth was that it is intended to be a :term:`Web server profile` 
that uses the browser side :term:`implicit flow`, 
with a simple sever side callback that extracts the fragment 
and passes it to the server for processing and verification.   
That is why :term:`Cross Origin Resource` sharing is not mentioned win that profile.

It is true 
that that profile could be used for a :term:`Canvas type JS app` in the browser 
accessing the endpoints as well.

Would your preference have been to make the :term:`basic client` use the :term:`code flow`?   
It is arguably similar in complexity at the end of the day,  
but with better security for :term:`Web Server type applications`.

I would probably just have the :term:`client` base64 decode the :term:`id_token` 
and forget calling the :term:`check_id endpoint`.   
If the client doesn't have the correct token endpoint 
and gives the :term:`client secret` to it checking the signature on the :term:`id_token` is not very useful:)

Regards
John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001596.html
--------------------------------------------------------------------------------------------------

All clients must register there :term:`redirect_url` and get a :term:`client_id`.

They are **not required** to use the :term:`client secret` if they are :term:`public clients`.

We talked about allowing a :term:`client_id` of  "public" 
and not requiring pre-registerd :term:`redirect_uri`, 
but the feedback was that **IdP were uncomfortable** giving :term:`access tokens` to unknown clients.

:term:`OAuth` recommends against :term:`public clients` with **unregistered** :term:`redirect_uri`.    

In a effort to have some balance we do have :term:`dynamic registration` for :term:`clients`.

If a user wants to revoke a :term:`client` not having all of them 
with the same :term:`client_id` is probably an advantage.

If it is something you think you need I am open to discussing it.

John B.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001599.html
--------------------------------------------------------------------------------------------------

I would prefer to have the :term:`Basic Client` use the :term:`code flow` 
for another reason: 
the **code flow** is the only one that's mandatory to implement for the :term:`server`. 
So what we have right now is advice for :term:`servers` to implement 
something that our advice to :term:`clients` say they don't have to.

  -- Justin

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001600.html
--------------------------------------------------------------------------------------------------

Both :term:`code` and ':term:`token id_token`'  should be :term:`mediatory to implement` for :term:`servers`.   

Is there a particular place that you are seeing that in the spec.  
I think that is a bug, if true.   I will look for it today.

If the WG did want code to be the only :term:`MTI flow` then we would defiantly need 
to change the :term:`basic profile` to :term:`code`.

John

.. glossary::

    MTI flow
    MTI Token
    MTI
    mandatory-to-implement
        may be Mandatory-To-Implement flow. Connect Basic MUST implement "code" and "token id_token".
        
    
        OAuth MTI token discussion is  http://www.ietf.org/mail-archive/web/oauth/current/msg07906.html


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001601.html
----------------------------------------------------------------------------------------------------

Hrm. Reading through the drafts again just now, it does clearly say that 
':term:`code`' and ':term:`token id_token`' are :term:`MTI`, 
so I'm not sure where I got that impression from. 
My mistake.

  -- Justin

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001602.html
----------------------------------------------------------------------------------------------------

No problem, sometimes even I am surprised by things that have snuck in 
or are left over from older versions.

Do you still prefer the :term:`code` follow for the :term:`basic client profile`?

John

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001603.html
----------------------------------------------------------------------------------------------------

Yes, I certainly do. **It's cleaner in design**, its pattern is **more proven**, 
and it can be implemented in all kinds of different clients, even 
lightweight Javascript ones. 

The :term:`implicit flow` is an optimization for **fewer network calls**, 
and it's always felt more like a **codified hack** than a real protocol flow to me. 
Whenever I've seen somebody pressed on the issue of whether 
or not their clients could really support the :term:`code flow`, 
they've admitted that yes, they could, but they didn't want to pay 
the time costs of a second round trip to the server.

We're also concentrating on the :term:`code flow` for our own Connect 
deployment, and we'll patch in the :term:`implicit flow` sometime later.

  -- Justin

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001604.html
----------------------------------------------------------------------------------------------------

As I recall it was Facebook and Google who were keen on the :term:`implicit flow`.

Part of the argument was that 
it was easier to get someone to implement it by dropping some :term:`JS code` 
on their site for the :term:`callback URI` and setting the :term:`id_token` as a :term:`cookie`.

It is a different approach than the more traditional library one, that fits the :term:`code flow` better.

I am not personally attached to the :term:`implicit flow`.

However we probably need wider feedback before changing the :term:`basic client profile`.

John 

.. note::
    
    Implicit Flow advantages:

    - Easier to deploy:  Just drop Facebook/Google provided Javscript on your pages.
    - ID Token can be user agent authenication cookie.   It is good for big cloud providers like Google/Facebook. 

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001627.html
----------------------------------------------------------------------------------------------------

> As I recall it was Facebook and Google who were keen on the implicit flow.

Actually, I think I suggested at least once to have ':term:`code`' be the
basic flow in OpenIDConnect. 
Not that I think the current approach of using 'token' to have been a bad decision. 
Just that I don't have a strong view either way.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001628.html
----------------------------------------------------------------------------------------------------

It was a close decision, as I recall.  
Both flows work almost equally well.  

The question was what would look simpler for a client to implement.  

I think the thought at the time was that we could produce a :term:`JS` 
that someone could drop on their site and have them up and running 
with the :term:`Basic profile` **without significant server side programming**.

One thing we are missing for the current Basic profile is that drop in JS code example.

Without the implicit example/template JS the :term:`code flow` may be simper for server side programers to understand.

John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001629.html
----------------------------------------------------------------------------------------------------

The :term:`token flow` is simpler *if* there's an existing corroborating server page 
with the returned javascript, which is the Facebook use case. 
Without that existing code, as John points out, 
it's no simpler than the code, and potentially more complex to implement securely.

  -- Justin

.. note::
    Javascript proof sample is required for Basic RP implementer.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001630.html
----------------------------------------------------------------------------------------------------

This sounds to me like an argument for us 
to create the JavaScript code so the promise of clients not having do any substantial programming 
to use Connect can come true.  
That's the reason we chose the :term:`implicit flow`, 
and why I think we should make it possible by getting the code written.

The process of writing the code might also give us valuable feedback on the specs, 
while we're still at Implementer's Draft stage.

Who would make sense to write that code?  
Maybe we could use **some directed funding** to make it happen???

                -- Mike


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001631.html
----------------------------------------------------------------------------------------------------

There are two approaches we could take with the JS code.

The **simple one** is the example code I posted earlier in the thread 
that the client puts at it :term:`redirect_uri` 
and it takes the :term:`fragment` and sends it to the :term:`Web server client` via POST for parsing.

The **more complicated one** would be to have the JS make the and process 
the response setting the validated :term:`id_token` as a cookie 
and save the :term:`user_info` attributes to :term:`HTML local storage` or post them back to the :term:`Web Client`.

That would be the most standalone example.   
Include a :term:`JS login widget` and it will set a :term:`openID cookie` once they are logged in. 
The Web Client just needs to validate the signature of the :term:`id_token`.

There are probably in-between states.  
There is probably example code around for most of that, 
someone needs to put it together and clean it up.

John  B

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001632.html
----------------------------------------------------------------------------------------------------

Let's add discussion of getting this code written to our agenda for the in-person working group meeting.

                -- Mike

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001636.html
----------------------------------------------------------------------------------------------------

+1

Unlike FB Connect, we do support :term:`asymmetric signature` 
so the :term:`signature validation` actually can be done by the JS client as well.

=nat

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001637.html
----------------------------------------------------------------------------------------------------

Yes, but the :term:`Basic client profile` is **only using symmetric signatures**.

The other issues is even if the :term:`JS client` can validate the signature 
the Web server still can't trust the validation,  
it needs to validate the assertion itself 
before releasing any of it's resources to the client.

I suppose one interesting option 
we haven't talked about is using the :term:`id_token` 
as the :term:`access_token` for additional API resources on the :term:`Client Web Server`.  
That should work quite nicely given the :term:`id_token` has the :term:`client` as it's :term:`audience` already.

John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001638.html
----------------------------------------------------------------------------------------------------

In the case of FB, 
only the way that the :term:`web server` can protect itself and
the user is to send the :term:`access token` to an undocumented api /app and get
the intended :term:`client_id`. 

That is just like the :term:`check id endpoint` except that
it is using :term:`access token` instead: i.e., it is a :term:`Check access token endpoint`. 
We could define such an extension endpoint.

Nat

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001639.html
----------------------------------------------------------------------------------------------------

The current proposal is to **add a hash** of the :term:`access_token` 
to the :term:`id_token` so that we would not need a separate :term:`access_token` :term:`introspection endpoint`.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001605.html
----------------------------------------------------------------------------------------------------

Actually, after Johns blog post about the vulnerability of OAuth as
authentication, I got a strong feedback from security and privacy community
that :term:`it is insane to send the token to the server`. 
The token was issued to the :term:`user agent` 
and sending that to the server constitutes security, privacy and policy breach. 
If we are to avoid sending token to the server, 
implicit flow is not simple any more. 
We have to use CORS or postMessage inter frame communication etc.

That is another reason to consider the possibility of making the code flow the default.

Nat Sakimura

.. note::

    To whom Implict tokens are to be issued  ?

        1. User Agent : User must grant to issue a token to UA where his privacy data is used at.
        2. User Agent and Client : Javascript and pages are controlled by Clients anyway.



http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001606.html
----------------------------------------------------------------------------------------------------

+1 pro :term:`code` as default flow
Gesendet mit BlackBerry® Webmail von Telekom Deutschland  



http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001625.html
----------------------------------------------------------------------------------------------------

Actually, I am not suggeting to through current Basic Client (side flow) Profile.

I was suggesting that perhaps it would be worthwhile to have appropriately
constrained Basic Server side flow Profile as well. 

Reading through some of the FB documentation, 
**I believe it does not have to be in the RFC format**, really. 
For those people who wants to read only a concise document, 
a white paper or a blog post like thing in a similar manner to
http://nat.sakimura.org/2012/01/20/openid-connect-nutshell/ would be more
valuable, I suppose.

=nat

.. note::

    Could be two basics:

    - Basic Client Side
    - Basic Server Side
      
http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001626.html
----------------------------------------------------------------------------------------------------

A correction: s/through/throw away/=

