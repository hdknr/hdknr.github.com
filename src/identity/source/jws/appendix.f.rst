Appendix F.  Detached Content
===================================

In some contexts, it is useful integrity protect content that is not
itself contained in a JWS object.  One way to do this is create a JWS
object in the normal fashion using a representation of the content as
the payload, but then delete the payload representation from the JWS,
and send this modified object to the recipient, rather than the JWS.
When using the JWS Compact Serialization, the deletion is
accomplished by replacing the second field (which contains
BASE64URL(JWS Payload)) value with the empty string; when using the
JWS JSON Serialization, the deletion is accomplished by deleting the
"payload" member.  This method assumes that the recipient can
reconstruct the exact payload used in the JWS.  To use the modified
object, the recipient reconstructs the JWS by re-inserting the
payload representation into the modified object, and uses the
resulting JWS in the usual manner.  Note that this method needs no
support from JWS libraries, as applications can use this method by
modifying the inputs and outputs of standard JWS libraries.

(draft27)

