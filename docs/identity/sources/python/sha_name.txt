.. code-block:: python

    import re

    def sha_name(alg):
        ''' 
            :param alg: Algorithms defined in JWA
        '''
        return "sha%(bits)s" % re.search(r'[HRE]S(?P<bits>\d+)$',alg).groupdict()
