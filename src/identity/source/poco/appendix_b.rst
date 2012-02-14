Appendix B.  Compatibility with OpenSocial
===========================================

This version of the Portable Contacts specification is currently wire-compatible 
with the overlapping portion of the OpenSocial RESTful Protocol version 0.8.1 [OpenSocial]. 
Specifically, any compliant OpenSocial RESTful Protocol 0.8.1 Provider 
is also a compliant Portable Contacts Provider, 
because they are specified to use the same Authorization methods (OAuth), 
Additional Path Information, Query Parameters, 
and Contact Schema. 
The OpenSocial and Portable Contacts communities chose to wire-align our respective specs 
in order to maximize widespread adoption of a single API for accessing people data.

It is our intention to maintain this compatibility going forward, so long as it is feasible, 
and so long as the changes required are compatible with the Goals and Approach of this spec. 
Although Portable Contacts is an independent spec, with a more limited scope than OpenSocial, 
any proposed changes to either this Portable Contacts spec or 
the OpenSocial RESTful Protocol should be considered in the context of both communities, 
and we should strive not to break compatibility 
unless it is truly necessary, 
e.g. if the goals of the two communities diverge significantly in the future.
