Mandatory-to-implement token type
====================================================================================================


http://www.ietf.org/mail-archive/web/oauth/current/msg07906.html
----------------------------------------------------------------------------------------------------

Stephen, as AD, brought up the question of :term:`mandatory-to-implement`
token types, in the IETF 82 meeting.  There was some extended
discussion on the point:

- Stephen is firm in his belief that it's necessary for interoperability.  
  He notes that mandatory to *implement* is not the same as mandatory to *use*.

- Several participants believe 
  that without a mechanism for requesting or negotiating a token type, 
  there is no value in having any type be :term:`mandatory to implement`.

Stephen is happy to continue the discussion on the list, and make his point clear.  
In any case, 
there was clear consensus in the room that we *should* specify a :term:`mandatory-to-implement` type, 
and that that type be :term:`bearer tokens`.  
This would be specified in the base document, 
and would make a normative reference from the base doc to the bearer token doc.

We need to confirm that consensus on the mailing list, 
so this starts the discussion.  
Let's work on resolving this over the next week or so, and moving forward:

1. Should we specify some token type as :term:`mandatory to implement`?  
   Why or why not (*briefly*)?

2. If we do specify one, which token type should it be?

Barry, as chair

.. note::
    - mandatory-to-implement
    - mandatory-to-use

http://www.ietf.org/mail-archive/web/oauth/current/msg07918.html
----------------------------------------------------------------------------------------------------

> 1. Should we specify some token type as mandatory to implement?  Why
> or why not (*briefly*)?

No, 
since I do not believe that the force of compliance with this one point of the spec 
will be enough to persuade those who don't want to use
whatever the MTI token type ends up being to use it. 
Let's say that we were to pick :term:`Bearer`, 
but Example.com decides to only support :term:`MAC` for their API. 
Is it correct to say that Example.com is not really doing OAuth2? 
I would argue no, 
since they're doing everything within spec to issue tokens, 
and the tokens that they're issuing are well defined and within spec as well. 
So then let's say, hypothetically, that in order comply with the letter of the law, 
they implement a :term:`Bearer token` as well as :term:`MAC`. 
But which type do they issue to clients? 
Clients have no way of choosing or discovering which what kind of token comes back (yet). 
If :term:`Bearer` is MTI, how do you even use another token type?

Which brings us to :term:`MTI` in clients,  [#]_
which makes even less sense. 
Let's say that I'm writing a client to talk to Example.com, 
which hands back :term:`MAC tokens`. 
I want to comply with the spec, 
so I implement :term:`Bearer` support in my client, 
code paths which will never see the light of day. 

Then there's the argument 
that a generic library is what's really meant by "client" here, 
and that those MUST follow the MTI guidelines. 
I also find this to be ludicrous, since client libraries will implement whatever servers support. 
A good client library will support *both* :term:`MAC` and :term:`Bearer` together, 
along with whatever magical tokens that haven't been dreamed up yet that are getting traction.

Ultimately, I think that our declaring something MTI is a position of
hubris that won't affect how people really use this thing.

 -- Justin

http://www.ietf.org/mail-archive/web/oauth/current/msg07921.html
----------------------------------------------------------------------------------------------------

.. [#] : refered.

I think this is really the key problem. 
To date, there isn't a unified library that clients and servers are using 
that could force this issue: 
every server/site is rolling their own oauth sdk, 
and they don't have much reason *now* to change that.  
If/when something emerged as being the oauth equivalent of openssl, 
then it would make sense to tighten requirements on such a library 
to achieve better interoperability. 
It would also coincide with actual real world _knowledge_ of 
what the appropriate MUST-IMPLEMENT's are instead of guessing.
All a :term:`mandatory requirement` will do now is alienate a lot implementations 
who are otherwise striving to be compliant.

So my bottom line to Stephen: 
defer this to a later recycle of the rfc.

Mike


http://www.ietf.org/mail-archive/web/oauth/current/msg07923.html
----------------------------------------------------------------------------------------------------

> 1. Should we specify some token type as mandatory to implement?  Why or
> why not (*briefly*)?

On the server - no. 
It makes no sense 
because the server **dictates** the token type 
so if it decides to never issue the mandated type, 
what's the point in implementing?

On the client, maybe. 
If the server knows that a client will always understand a set of token types, 
it can choose to use that and ensure interop (or not). 
In practice, 
**mandating will add no real interop value**. 
Almost every client will hard-code the token types 
it needs to understand and providers are not likely to support more than one or to change it. 
We can mandate a type for 'generic clients' so that libraries support both, 
but it won't actually make any difference.

Bottom line, 
this is a red herring. 
OAuth doesn't really provide this level of interop and was never designed for that. 
In the future, 
when we have more interop web APIs (photos, social, etc.) 
and we have real world experience with discovery, 
this will be important. But that's a few years away (at least).
 
> 2. If we do specify one, which token type should it be?

This is a no win situation. 
Most providers will ignore a requirement to support MAC, 
or will support it but will not see much usage because most developers 
when given the choice will go with :term:`Bearer`. 
Mandating :term:`Bearer` will be ignored by providers who want better security 
and will most likely render :term:`MAC` pointless. 
If we mandate :term:`Bearer`, 
I see no point in even publishing :term:`MAC` 
as it will turn into a purely theoretical exercise.

Given the history of this group, 
no change is the only likely consensus.

EHL

http://www.ietf.org/mail-archive/web/oauth/current/msg07973.html
----------------------------------------------------------------------------------------------------

Re: "So, pick one (my strong personal preference) or establish and
document why you're not picking one seem to me to be the choices
available."

We don't have discovery done (enough) 
yet to lean on it in the core spec, 
but if we did I'd be in favor of something that says 
that you must implement either an MTI token 
OR a discovery mechanism that advertises at least one token.  
Would that be workable?  

We could bang on the discovery stuff in pretty short order I think if we needed to.

-bill



