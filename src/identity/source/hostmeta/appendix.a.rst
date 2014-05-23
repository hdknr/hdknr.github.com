.. _hostmeta.jrd:

Appendix A.  JRD Document Format
==============================================================================

The JRD document format -- a general-purpose XRD 1.0 representation
-- uses the JavaScript Object Notation (JSON) format defined in
[RFC4627].  JRD uses the same elements and processing rules described
in Section 3.1.  

The JRD format is designed to include the same base
functionality provided by the XML format, with the exception of
extensibility, as extensibility is beyond the scope of this
specification.

The client MAY request a JRD representation using the HTTP "Accept"
request header field with a value of "application/json".  The server
MUST include the HTTP "Content-Type" response header field with a
value of "application/json".  Any other "Content-Type" value (or lack
thereof) indicates that the server does not support the JRD format.

Alternatively, the client MAY request a JRD representation by
requesting the "host-meta.json" well-known document, by making a GET
request for "/.well-known/host-meta.json", following the same process
used for "/.well-known/host-meta".  If the server does not support
serving a JRD representation at this location, the server MUST
respond with an HTTP 404 (Not Found) status code.

XRD elements are serialized into a JSON object as follows:

-  The XML document declaration and "XRD" element are discarded.

-  The "Subject" element is included as a name/value pair with the
   name 'subject', and value included as a string.

-  The "Expires" element is included as a name/value pair with the
   name 'expires', and value included as a string.

-  "Alias" elements are included as a single name/value pair with the
   name 'aliases', and value a string array containing the values of
   each element in order.

-  "Property" elements are included as a single name/value pair with
   the name 'properties', and value an object with each element
   included as a name/value pair with the value of the "type"
   attribute as name, and element value included as a string value.
   The values of properties with empty values (i.e., using the
   REQUIRED "xsi:nil='true'" attribute) are included as null.  If
   more than one "Property" element is present with the same "type"
   attribute, only the last instance is included.

-  "Link" elements are included as a single name/value pair with the
   name 'links', and value an array with each element included as an
   object.  Each attribute is included as a name/value pair with the
   attribute name as name, and value included as a string.

-  "Link" child "Property" elements are included using the same
   method as XRD-level "Property" elements using a name/value pair
   inside the link object.

-  "Link" child "Title" elements are included as a single object with
   the name 'titles', and value an object with each element included
   as a name/value pair with the value of the "xml:lang" attribute as
   name, and element value included as a string value.  The names of
   elements without an "xml:lang" attribute are added with the name
   'default'.  If more than one "Title" element is present with the
   same (or no) "xml:lang" attribute, only the last instance is
   included.

-  The conversion of any other element is left undefined.

For example, the following XRD document...

.. code-block:: xml

 <?xml version='1.0' encoding='UTF-8'?>
 <XRD xmlns='http://docs.oasis-open.org/ns/xri/xrd-1.0'
      xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>

   <Subject>http://blog.example.com/article/id/314</Subject>
   <Expires>2010-01-30T09:30:00Z</Expires>

   <Alias>http://blog.example.com/cool_new_thing</Alias>
   <Alias>http://blog.example.com/steve/article/7</Alias>

   <Property type='http://blgx.example.net/ns/version'>1.2</Property>
   <Property type='http://blgx.example.net/ns/version'>1.3</Property>
   <Property type='http://blgx.example.net/ns/ext' xsi:nil='true' />

   <Link rel='author' type='text/html'
         href='http://blog.example.com/author/steve'>
     <Title>About the Author</Title>
     <Title xml:lang='en-us'>Author Information</Title>
     <Property type='http://example.com/role'>editor</Property>
   </Link>

   <Link rel='author' href='http://example.com/author/john'>
     <Title>The other guy</Title>
     <Title>The other author</Title>
   </Link>


   <Link rel='copyright'
         template='http://example.com/copyright?id={uri}' />
 </XRD>

...is represented by the following JRD document:

.. code-block:: javascript

 {
   "subject":"http://blog.example.com/article/id/314",
   "expires":"2010-01-30T09:30:00Z",

   "aliases":[
     "http://blog.example.com/cool_new_thing",
     "http://blog.example.com/steve/article/7"],

   "properties":{
     "http://blgx.example.net/ns/version":"1.3",
     "http://blgx.example.net/ns/ext":null
   },

   "links":[
     {
       "rel":"author",
       "type":"text/html",
       "href":"http://blog.example.com/author/steve",
       "titles":{
         "default":"About the Author",
         "en-us":"Author Information"
       },
       "properties":{
         "http://example.com/role":"editor"
       }
     },
     {
       "rel":"author",
       "href":"http://example.com/author/john",
       "titles":{
         "default":"The other author"
       }
     },
     {
       "rel":"copyright",
       "template":"http://example.com/copyright?id={uri}"
     }
   ]
 }


Note that the "Subject" and "Alias" elements are NOT RECOMMENDED in
the context of host-meta documents, and are included in the example
for completeness only.

