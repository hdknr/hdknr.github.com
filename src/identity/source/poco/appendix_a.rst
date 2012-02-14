Appendix A.  Example
=======================

Here is a sample request and response 
that illustrates much of Portable Contacts. 
For simplicity, authorization information is not shown in the request.

Sample request (via HTTP GET):

::

    http://sample.site.org/path/to/api/@me/@all?startIndex=10&count=10&sortBy=displayName

Sample response (JSON):

.. code-block:: javascript 

    {
      "startIndex": 10,
      "itemsPerPage": 10,
      "totalResults": 12,
      "entry": [
        {
          "id": "123",
          "displayName": "Minimal Contact"
        },
        {
          "id": "703887",
          "displayName": "Mork Hashimoto",
          "name": {
            "familyName": "Hashimoto",
            "givenName": "Mork"
          },
          "birthday": "0000-01-16",
          "gender": "male",
          "drinker": "heavily",
          "tags": [
            "plaxo guy",
            "favorite"
          ],
          "emails": [
            {
              "value": "mhashimoto-04@plaxo.com",
              "type": "work",
              "primary": "true"
            },
            {
              "value": "mhashimoto-04@plaxo.com",
              "type": "home"
            },
            {
              "value": "mhashimoto@plaxo.com",
              "type": "home"
            }
          ],
          "urls": [
            {
              "value": "http://www.seeyellow.com",
              "type": "work"
            },
            {
              "value": "http://www.angryalien.com",
              "type": "home"
            }
          ],
          "phoneNumbers": [
            {
              "value": "KLONDIKE5",
              "type": "work"
            },
            {
              "value": "650-123-4567",
              "type": "mobile"
            }
          ],
          "photos": [
            {
              "value": "http://sample.site.org/photos/12345.jpg",
              "type": "thumbnail"
            }
          ],
          "ims": [
            {
              "value": "plaxodev8",
              "type": "aim"
            }
          ],
          "addresses": [
            {
              "type": "home",
              "streetAddress": "742 Evergreen Terrace\nSuite 123",
              "locality": "Springfield",
              "region": "VT",
              "postalCode": "12345",
              "country": "USA",
              "formatted": "742 Evergreen Terrace\nSuite 123\nSpringfield, VT 12345 USA"
            }
          ],
          "organizations": [
            {
              "name": "Burns Worldwide",
              "title": "Head Bee Guy"
            }
          ],
          "accounts": [
            {
              "domain": "plaxo.com",
              "userid": "2706"
            }
          ]
        }
      ]
    }

Sample response (XML):

.. code-block:: xml

    <response>
    
     <startIndex>10</startIndex>
     <itemsPerPage>10</itemsPerPage>
     <totalResults>12</totalResults>
     <entry>
    
      <id>123</id>
      <displayName>Minimal Contact</displayName>
     </entry>
     <entry>
      <id>703887</id>
    
      <displayName>Mork Hashimoto</displayName>
      <name>
       <familyName>Hashimoto</familyName>
       <givenName>Mork</givenName>
    
      </name>
      <birthday>0000-01-16</birthday>
      <gender>male</gender>
      <drinker>heavily</drinker>
    
      <tags>plaxo guy</tags>
      <tags>favorite</tags>
      <emails>
       <value>mhashimoto-04@plaxo.com</value>
    
       <type>work</type>
       <primary>true</primary>
      </emails>
      <emails>
       <value>mhashimoto-04@plaxo.com</value>
    
       <type>home</type>
      </emails>
      <emails>
       <value>mhashimoto@plaxo.com</value>
       <type>home</type>
    
      </emails>
      <urls>
       <value>http://www.seeyellow.com</value>
       <type>work</type>
      </urls>
    
      <urls>
       <value>http://www.angryalien.com</value>
       <type>home</type>
      </urls>
      <phoneNumbers>
    
       <value>KLONDIKE5</value>
       <type>work</type>
      </phoneNumbers>
      <phoneNumbers>
       <value>650-123-4567</value>
    
       <type>mobile</type>
      </phoneNumbers>
      <photos>
       <value>http://sample.site.org/photos/12345.jpg</value>
       <type>thumbnail</type>
    
      </photos>
      <ims>
       <value>plaxodev8</value>
       <type>aim</type>
      </ims>
    
      <addresses>
       <type>home</type>
       <streetAddress><![CDATA[742 Evergreen Terrace
    Suite 123]]></streetAddress>
       <locality>Springfield</locality>
    
       <region>VT</region>
       <postalCode>12345</postalCode>
       <country>USA</country>
       <formatted><![CDATA[742 Evergreen Terrace
    Suite 123
    Springfield, VT 12345 USA]]></formatted>
    
      </addresses>
      <organizations>
       <name>Burns Worldwide</name>
       <title>Head Bee Guy</title>
      </organizations>
    
      <accounts>
       <domain>plaxo.com</domain>
       <userid>2706</userid>
      </accounts>
     </entry>
    
    </response>


