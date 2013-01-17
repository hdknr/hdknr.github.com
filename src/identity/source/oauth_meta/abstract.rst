Abstract
==================

This specification defines an extensible :term:`metadata` member 
that may be inserted into the :doc:`OAuth 2.0 <oauth>` responses 
to assist the :term:`clients` to process those responses.  

It is expressed as a member called ":term:`_links`"
that is inserted as the top level member in the responses.  

It will allow the client to learn 
where the members in the response could be used and how, etc.  
Since it is just a member, 
any client that does not understand this extension should not break 
and work normally while supporting clients can utilize the metadata to its advantage.

( http://tools.ietf.org/html/draft-sakimura-oauth-meta-01 )

( draft 01 )

