.. code-block:: python

    def to_base64url(src):
        return base64.urlsafe_b64encode(src).replace('=','') 
    
    def from_base64url(src):
        return base64.urlsafe_b64decode(src + '=' * (len(src) % 4 ))
