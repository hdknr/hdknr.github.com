Abstract
========================

This document proposes an additional endpoint for OAuth authorization servers, 
which allows clients to notify the authorization server that
a previously obtained refresh or access token is no longer needed.

This allows the authorization server to clean up security credentials.  
A revocation request will invalidate the actual token and, 
if applicable, other tokens based on the same authorization grant

( http://tools.ietf.org/html/rfc7009 )
