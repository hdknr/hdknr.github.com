Response types clarification
==========================================


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001588.html
----------------------------------------------------------------------------------------------------

oHi all,

I'm trying to catch up with the Implementors Draft and need some advice 
from the group.

Is it correct that ":term:`code`" is the only :term:`response type`, 
which is delivered to the :term:`client` via :term:`URI query parameter`? 
For all other :term:`response types`, 
the response parameters are encoded within the :term:`URI fragment`.

Furthermore, 
is the :term:`client` always issued an :term:`access token` _and_ an :term:`id_token` 
for :term:`scope` ":term:`openid`" and :term:`response type` ":term:`code`"?

thanks in advance,
Torsten.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001590.html
----------------------------------------------------------------------------------------------------

> Is it correct that "code" is the only response type, which is delivered to the client via URI query parameter? For all other response types, the response parameters are encoded within the URI fragment.
Yes
> 
> Furthermore, is the client always issued an access token _and_ an id_token for scope "openid" and response type "code"?

The response from the :term:`Authorization server` is :term:`code` as was asked for.

The :term:`Token endpoint` includes :term:`id_token` in it's response as an extra parameter. 

So strictly speaking Yes :term:`id_token` is **always issued** if the :term:`scope` is ':term:`openid`'  
(scope is a single value with spaces, so don't say includes) and the :term:`response_type` is :term:`code`.

However the :term:`response type` is :term:`code` and **only code**. 

.. list-table::

    *   - scope
        - response_type
        - response
        - in

    *   - openid
        - code
        - code 
        - query 

    *   - openid
        - token id_token
        - token id_token
        - fragment

The :term:`id_token` is only returned 
if :term:`code` is exchanged at the :term:`token endpoint` for and :term:`access_token` and :term:`id_token`.   

So I suppose you could avoid getting :term:`id_token` by not exchanging :term:`code`, 
but I don't think anyone is going to think that is a good idea.

The problem is that **response)type** only controls 
what comes back from the :term:`Authorization endpoint`, and not the :term:`token endpoint`.

The only option 
we found was overloading a :term:`scope` to change the behaviour of the :term:`token endpoint` 
to return the extra value.

The :term:`token endpoint response` is direct, 
so size is not a big issue.  
It was simpler to always return it from that endpoint 
than create a complicated way of asking for it from the :term:`token endpoint`.

Worst case the response is a bit bigger, but the client ignores the extra parameter.

John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001591.html
----------------------------------------------------------------------------------------------------

Hi John,

thanks for the clarification.

So all :term:`response types` containing the string value ":term:`id_token`" cause the 
authorization server to directly return a :term:`id_token` 
(along with all other parameters) to the :term:`client` via :term:`fragment`?

regards,
Torsten.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001595.html
----------------------------------------------------------------------------------------------------

:term:`Response types` are **single values**.   
(I am starting to hate Erin's compromise) [#]_

.. [#]  What compromise ?

The :term:`response types` are documented in: http://openid.bitbucket.org/oauth-v2-multiple-response-types-1_0.html

The :term:`response types` 
"code id_token",  
"id_token token", and 
"code id_token token"  
MUST return a :term:`id_token` and the response **SHOULD** be **fragment encoded**.

Now you are asking yourself 
why is that SHOULD be :term:`fragment encoded` as opposed to MUST be fragment encoded.

The reason for that is that the :term:`response_type` registration 
is leaving wiggle room to use the same **response type with post message** as well.

For that to work the client would need to register a :term:`JS Origin` 
and DOM Channel Names(or pick a fixed strings).  

We did stub in **post message configuration parameters**, 
but removed them due to there not being a OAuth spec yet.   

Probably more than the yes you were looking for, 
but the history provides some perspective.

John B.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001608.html
----------------------------------------------------------------------------------------------------

Hi John,

thanks again for the clarification. HTTP/HTML can be so complicated :-(

Another question crossed my mind: 
The number of :term:`response types` really struck and confused me 
during my first read and I assume this will happen to others as well. 
Why not significantly reduce the number of response types by

- not combining :term:`code` and :term:`token` and
- just using "token" instead of all combinations of id_token and token ?

The response type "token" could cause the OP to return both the id_token 
and the access token in the :term:`fragment`, 
which is similar to the response of the :term:`tokens endpoint`. 
I know this would return tokens the client is potentially not interested in. 
But this seems to be accepptable for the code response type.

regards,
Torsten.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001610.html
----------------------------------------------------------------------------------------------------

> - just using "token" instead of all combinations of id_token and token ?
>
> The response type "token" could cause the OP to return both the 
> id_token and the access token in the fragment, which is similar to the 
> response of the tokens endpoint. I know this would return tokens the 
> client is potentially not interested in. But this seems to be 
> accepptable for the code response type.
>

I actually rather like this approach. 
It keeps the question of whether or not 
you want OpenID confined to the value of the 'scope' field 
(that is, presence of an 'openid' value in there), 
and it makes serialization of the ID Token just a part of the access token output, 
like the code flow with the token endpoint. 
Of course we still have to profile how it gets encoded, 
but it's ultimately another field in the token output.

  -- Justin

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001611.html
----------------------------------------------------------------------------------------------------

That was the way we originally had it.   
Later on people thought that using the OAuth multi-response type was more OAuth friendly.

Originally if you had the scope openid:

1 response_type=code   both code and id_token were query encoded in the response
2 response_type=token  both access_token and id_token were fragment encoded.

There was no way to just get code or access_token, 
and no way to get just id_token.

It was simpler I will give you that.

It is a bit different from adding id_token to the token endpoint in that 
there is no OAuth mechanism for controlling the response from the endpoint.  
I suppose the alternative would have been to add an extra parameter to the token endpoint request 
to say if you wanted a id_token.

Again the problem is that the :term:`response types` are not really combinations of token id_token 
but entirely new response types that contain the substrings token or id_token to confuse developers.

John

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001612.html
----------------------------------------------------------------------------------------------------

> That was the way we originally had it.   Later on people thought that using the OAuth multi-response type was more OAuth friendly.
>
> Originally if you had the scope openid:
> 1 response_type=code   both code and id_token were query encoded in the response

Query encoding id_token leads to increased privacy risks.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001613.html
-----------------------------------------------------------------------------------------------------

Yes query encoding of id_tokens runs the risks of leaking them through logs, proxys, 
and most of all through :term:`referrer`.

One of the reasons for the change in the later drafts.

You can protect against :term:`referrer leaking` 
but that requires a level of client sophistication that is unlikely in the wild.

I should mention that :term:`POST responses` were an option in openID 2.0, 
but are not in OAuth (for lots of good reasons).

The :term:`fragment encoded response` is also less size constrained in many cases, 
especially if the JS is using POST to push the parameters to the server.

.. note::

    No POST response in OAuth 2.0

John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001614.html
----------------------------------------------------------------------------------------------------

Hi,

John Bradley <ve7jtb at ve7jtb.com> schrieb:

>Yes query encoding of id_tokens runs the risks of leaking them through
>logs, proxys, and most of all through referrer.
>

I'm getting confused. 
Didn't you say in your response to my posting regarding id tokens 
as URI query parameters security was not the reason for not transmitting id tokens that way?

>One of the reasons for the change in the later drafts.
>
>You can protect against referrer leaking but that requires a level of
>client sophistication that is unlikely in the wild.
>
>I should mention that POST responses were an option in openID 2.0, but
>are not in OAuth (for lots of good reasons).
>
>The fragment encoded response is also less size constrained in many
>cases, especially if the JS is using POST to push the parameters to the
>server.
>

What is the difference between the POST binding and a JS pushing the token via POST request?

regards,
Torsten. 

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001615.html
----------------------------------------------------------------------------------------------------

The redirect response with a id_token is no more likely 
to leak than a openID 2 redirect response.

The main reason was functionality the :term:`fragment response` works 
for both web servers and JS clients.  

Leaking the :term:`id_token` is more of a **privacy problem** than a **security one**.  

Breno is correct that :term:`fragment` has better privacy less leakage.  

The difference between a :term:`post redirect` and JS pushing via POST 
is the large **browser warning** 
if you are going between https and non https endpoints 
and other strange side effects of cross origin POSTs.

The JS version is less prone to freak out users.

John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001617.html
----------------------------------------------------------------------------------------------------

I appreciate that you are trying to catch up with the logic of decisions made 
over a multi year development process that involved a large number of people.

I am trying to fill in the colour as best as I can remember, as one of the editors.

OAuth 2 itself also changed under us during the process as well.

Fortunately or unfortunately making breaking changes at this point 
will require a supermajority of the WG, now that we have implementers drafts in peoples hands.

Non normative changes are not going to be a big issue 
if we find things that need further clarification or outright bugs.

I expect that additional profiles for things like code flow are probably a good idea 
even if we leave the Basic Client profile as is.

We just need to decide if they are normative and part of the specs or non-normative implementers guides.    
Basic is a bit of a mix as it was intended to work as a standalone document 
without referencing the other parts of the specs.

I am still trying to figure out 
why you are getting the impression that the Basic profile is just for JS clients?

John B.

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001640.html
----------------------------------------------------------------------------------------------------

Hi John,

Am 21.02.2012 20:48, schrieb John Bradley:
> I am still trying to figure out why you are getting the impression that the Basic profile is just for JS clients?

I've got a basic understanding of how it is supposed to work for web 
applications. 
But I suspect I'm not the only one considering it rather complicated.

Let me revisit the flow (after sucessful login):

1) the OP redirects back to the redirect_uri (client web site)
2) the web site uploads HTML and pieces of JS to the client
3) the JS code extracts the id_token from the URL fragment and posts it to its backend

So the RP implementation requires a combination of backend and client side code. 
Furthermore, 
the RP needs to process two (or more? - see below) calls to perform the login. 
In contrast, 
a login based on the code flow can be implemented in the backend 
only and requires only a single request on the RP.

In my opinion, 
the Basic profile is opimized from a OP perspective 
as it minimizes calls and (potentially) shared state on the OP's side whereas 
the :term:`code flow` is easier to use from a RPs perspective.

Further questions regarding Basic profile:
How are client and server state synchronized with respect to the user identity after step (3)? 
Independently, 
based on the id_token that is evaluated on either side? 
Or will the client fetch additional data?

I assume URL length restrictions do not hold for **fragements**, 
otherwise there would be limitations regarding id_token/access_token size.

What is your story for existing OpenID 2.0 RP? 
Do you intend to propose them to migrate to the Basic profile?

regards,
Torsten.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001641.html
----------------------------------------------------------------------------------------------------

> So the RP implementation requires a combination of backend and client side code. Furthermore, the RP needs to process two (or more? - see below) calls to perform the login. In contrast, a login based on the code flow can be implemented in the backend only and requires only a single request on the RP.

The JS for POSTing the fragment to the backend could be cached 
as part of the initial page load at the RP,  
the redirect from the Authorization endpoint would trigger the cached JS 
and the result would be a single POST to the RP.

The response from the post can set browser cookies, 
allowing a simple client less overhead in maintaining state with the backend call.

I don't have any special personal attachment to the implicit flow,  
others can probably better defend it.

> In my opinion, the Basic profile is opimized from a OP perspective as it minimizes calls and (potentially) shared state on the OP's side whereas the code flow is easier to use from a RPs perspective.
> 

That may depend on the RP, but point taken.

> Further questions regarding Basic profile:
> How are client and server state synchronized with respect to the user identity after step (3)? Independently, based on the id_token that is evaluated on either side? Or will the client fetch additional data?
> 

I don't understand the question client and server are a bit ambiguous. 

In the above flow the Web Server is the client,  
It has a bit of JS to help relay the message and get around using a POST redirect.  

I would not call the browser the client in that case. 

It is possible that there are cases where you would have a canvas app in the browser that is interacting with the OAuth endpoints as well as a WebServer that is using the id_token to grant access to some of it's resources.   
That is however a much more complicated case.

> I assume URL length restrictions do not hold for fragements, otherwise there would be limitations regarding id_token/access_token size.
> 
> What is your story for existing OpenID 2.0 RP? Do you intend to propose them to migrate to the Basic profile?

Migrate to Connect,  
Basic if it works for them or one of the other flows if they work better.   

Basic is not intended to be the bast way to implement Connect, 
only a proposal for the simplest with basic functionality.

John


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001618.html
----------------------------------------------------------------------------------------------------


John, 
thanks for the background. This leaves me with a major question though:

> That was the way we originally had it.   Later on people thought that using the OAuth multi-response type was more OAuth friendly.
>
> Originally if you had the scope openid:
> 1 response_type=code   both code and id_token were query encoded in the response

Maybe I'm missing something, 
but in the "code" flow, you don't get back an id_token in that response. 
You get back a code, 
and that code can be exchanged for an access token and an id_token, 
since you asked for something that includes the "openid" scope. From Standard, section 2.2.1:

code

    When supplied as the value for the response_type parameter, a
    successful response MUST include an Authorization Code as defined in
    the OAuth 2.0 specification. Both successful and error responses
    MUST be added as parameters to the query component of the response.
    All tokens are returned from the Token Endpoint. Authorization
    Servers MUST support this response_type. 

So the whole issue of query-encoding the id_token isn't even an option here. 
It *is* an option 
if you're asking for something akin to "code id_token", 
but that wasn't on the table. 
In the current spec, those are both defined as :term:`fragment encoded` anyway.

> 2 response_type=token  both access_token and id_token were fragment encoded.
>
> There was no way to just get code or access_token, and no way to get just id_token.

The former, yes, there is: 
just don't include the "openid" scope. 

The latter, no. 
But if you ask for a token with just the "openid" scope and don't ask for any other permissions, 
the server *could* give you a null or empty or otherwise useless access token there, 
if it wanted to. 
I agree that if this is a real and viable use case, 
then it should be a separate kind of :term:`response_type`, 
but I'm not seeing that right now.

> It was simpler I will give you that.
>
> It is a bit different from adding id_token to the token endpoint in that there is no OAuth mechanism for controlling the response from the endpoint.  I suppose the alternative would have been to add an extra parameter to the token endpoint request to say if you wanted a id_token.

No, again, 
that's what the scope already handles. 
If we didn't have a standardized :term:`scope` value, then I'd agree with this.

  -- Justin


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001619.html
----------------------------------------------------------------------------------------------------

> So the whole issue of query-encoding the id_token isn't even an option here. It *is* an option if you're asking for something akin to "code id_token", but that wasn't on the table. In the current spec, those are both defined as fragment encoded anyway.

Having :term:`id_token` returned in the front channel was one of the early must haves from the major IdP.   
Given that in the early days 
we returned :term:`id_token` query encoded in the front channel and from the :term:`token endpoint`.  
It looked like a hack.   
There was no way to change the semantics of :term:`code`.   
With the :term:`multi token response type` change around draft 19 of OAuth I think,  
Google and Facebook decided that was the best way to indicate the :term:`response_type`, 
rather than overloading the semantics of :term:`scopes`.

Currently if you ask for code it is defined in the OAuth 2 core spec 
and you get code back just as you would expect, the same goes for token.  
We avoided reinterpreting the OAuth spec as much as possible.
The permissible way to ask for multiple tokens is the return type and that is what we are currently doing.

> 
>> 2 response_type=token  both access_token and id_token were fragment encoded.
>> 
>> There was no way to just get code or access_token, and no way to get just id_token.
> 
> The former, yes, there is: just don't include the "openid" scope. The latter, no. But if you ask for a token with just the "openid" scope and don't ask for any other permissions, the server *could* give you a null or empty or otherwise useless access token there, if it wanted to. I agree that if this is a real and viable use case, then it should be a separate kind of response_type, but I'm not seeing that right now.
> 

The thing is that if you don't include the openid scope 
you are not doing openid Connect and our spec has nothing to say in the matter.   
So removing the :term:`openid` scope 
so that the IdP can't tell if it is a connect request or some other OAuth request is not a real option.

The only thing I might change at this point on :term:`response_type` 
if I had a do over would be to use underscores rather than spaces to reduce confusion.   
Other than that I don't think we have a problem.

In reality 
a client will only use a single response type appropriate for it.   
They are not dynamically changing these things.   
If you want code as a query parameter just ask for 'code' all the options are available 
to the clients without confusing it with the scopes.


>> It was simpler I will give you that.
>> 
>> It is a bit different from adding id_token to the token endpoint in that there is no OAuth mechanism for controlling the response from the endpoint.  I suppose the alternative would have been to add an extra parameter to the token endpoint request to say if you wanted a id_token.
> 
> No, again, that's what the scope already handles. If we didn't have a standardized scope value, then I'd agree with this.
> 

Again if you remove the :term:`openid` scope it is not openid.  
That is the scope that asks for the user_info endpoint and the user_id.

John

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001620.html
---------------------------------------------------------------------------------------------------

On not being OpenID: 
I would say that 
if you're not getting an ID Token back, 
you're not doing OpenID Connect, you're just doing OAuth2. 
If you happen to be doing OAuth2 against something that has a User Info Endpoint, that's fine, 
but it's not binding you to the user's session. 
It's definitely the right thing to avoid mucking about with OAuth2 wherever possible.

But the question being addressed below was 
"how do I know when to include the ID Token?", 
and I think it should break down as follows 
(assuming user grants access and all else is validated):

- if the request to the token endpoint includes the scope ':term:`openid`', 
  throw the :term:`id token` into the :term:`JSON response`
- if the request to the :term:`authorization endpoint` is for type ':term:`token`' and 
  the :term:`scope` includes ':term:`openid`', 
  throw the :ref:`id token` into the :term:`fragment`
- if the request to the authorization endpoint is for type ':term:`code id_token`' 
  and the scope includes ':term:`openid`', 
  throw the :term:`id token` into the :term:`fragment` 
  along with the :term:`code` 
  (again, avoids the query parameter leakage issue brought up before)
- if the request to the :term:`authorization endpoint` is for type ':term:`code token`' 
  and the scope includes ':term:`openid`', 
  throw the :term:`id token` and the :term:`access token` into the :term:`fragment along` with the :term:`code`

What I'm saying is that #3 above is an odd special case that could be subsumed by #4 above. 
This all gets rid of the need for the id_token response type entirely. 
Apart from being a breaking change, 
I don't see how this doesn't cover the use cases described below.

  -- Justin

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001621.html
----------------------------------------------------------------------------------------------------


The current specs have much simpler rules than the ones proposed below.  They are:

-               If response_type includes id_token, return an ID Token.
-               If response_type includes token, return a Token.
-               If response_type includes code, return a Code.

These can be mixed and matched as meets the Client's needs.

I don't see a good reason to make it any more complicated than that.

                                                            -- Mike

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001622.html
----------------------------------------------------------------------------------------------------

( refer to http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001620.html )
 
I don't see why this is simpler. It's actually more obscure to developers. 
The scope 'openid' refers to scope of access -- 
**namely the request to learn the user's identifier at the issuer**.


http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001623.html
------------------------------------------------------------------------------------------------

I agree with Breno, 
keeping :term:`scopes` and :term:`response types` **separate** will cause fewer problems down the road.

We have a number of new response types registered,  
(I may have to hurt the next person who talk about them being com posable.)

Each :term:`response_type` clearly defines 
what is returned from the authorization server, 
and how it is to be returned (ignoring grey area for post message).

The :term:`openid` scope makes the protocol :term:`openid` asking for a authentication grant.  
e.g. Do you want to log into x and give them access to your user_id.   Simple.

The openid protocol requires that :term:`id_token` is always returned 
from the token endpoint when exchanging code.  Simple.

The registered responstypes define what is returned from the authorization endpoint and how.  Simple.  

Removing some of the return_types and overloading the openid scope with more semantics is more complicated.

My opinion
John B.

.. note::

    scope=openid

        - authentication assertion -  identifier user@idp is asserted.
        - standard user attributes -  access token to User Info endpoint


    authentiation assertion:

        - format 
            - id_token

        - response 

            - indirectly in URL fragment  ( only if specified response_type has id_token)
            - directly  from tokne endpoint
            
    standard user attributes

        - User Info JSON

http://lists.openid.net/pipermail/openid-specs-ab/Week-of-Mon-20120220/001624.html
----------------------------------------------------------------------------------------------------

Yes.

As I understand, 
OAuth's :term:`response_type` parameter tells 
**what is to be returned** by the :term:`Authorization Endpoint`.
We should stick to the semantics of it and should not alter it.

Perhaps we could state it in our specs, but that actually is something that
OAuth spec. really should do.

FYI, I wrote a blog post with a table showing what are to be returned in
each cases.

Hope this helps.

http://nat.sakimura.org/2012/02/22/the-relationship-between-endpoint-responses-and-response_type-scope-pair/

=nat
 
.. note::
    response_type = what is(are in Connect) to be returned.

