2.5.2.  Aggregated and Distributed Claims
--------------------------------------------------------

Aggregated and distributed Claims are represented by a JSON object including folowing claims:

.. glossary::

    _source

        For Aggregated claim, this value is JWT string to contain the name of the claim.

        For Distributed clamin, this value is URL of the endpoint to get JSON.

        Otherwise, value is  a key in "_sources" mapper in JSON.
        
    _access_token
    
        REQUIRED if this claim is distributed.   


And at the same JSON node level, a mapper can be used to  define Aggreated and Distributed Claims:


.. glossary::
    
    _sources
    
        Disctionay JSON object. Keys MUST be unique for other A & D Claims to index. 
        Values are concrete A & D Claims.


The following is a non-normative response: 

.. code-block:: json

    {
        .... 
        "address"        : { "_source": "jwt_header.jwt_2nd.jwt_3rd" },
        "pension_number" : { "_source": "http://japan.inc/pension/number", "_access_token" :  "ksj3n283dke"}, 
        ....
    }

If a single source holds multiple claims, a dictinaly "_sources" can hold this JSON objects:

.. code-block:: json

    {
        .... 
        "address":       : { "_source": "mybank" },
        "bank_account"   : { "_source": "mybank" },
        "pension_number" : { "_source": "mypension"},
        "pension_office" : { "_source": "mypension"},
        ....

        "_sources" : { 
          "mybank" : { "_source": "jwt_header.jwt_2nd.jwt_3rd" },
          "mypension" : { "_source": "http://japan.inc/pension/number", "_access_token" :  "ksj3n283dke"}
        }
    }
        
Where a aggregated JWT, contains the following JSON:

.. code-block:: json

    {
        "address" : {
            "country" : "Japan",
            "postal_code : "1500053",
            "region" : "Tokyo",
            .....
        },
        "bank_account" :  "0000-1111-2222"
    }


and the distributed endpoint returns the following JSON:

.. code-block:: json

    {
        "pension_number" : "1432143",
        "pension_office" : "Shibuya,Tokyo"
    }

