======
enum
======

.. contents::
    :local:

Python 3.4から
============================

- :mod:`enum`

Python 2.7 だとpipで
============================

.. code-block:: bash

    $ pip install enum34


mixinとかできない
------------------------

.. code-block:: python

    from enum import Enum
    
    class AlgSign(Enum):
        SIGN1 = 'SIGN1'
        SIGN2 = 'SIGN2'
    
    class AlgEnc(Enum):
        SIGN1 = 'SIGN1'
        SIGN2 = 'SIGN2'
    
    class Alg(AlgSign, AlgEnc):
        pass

TypeErrorです:
    

.. code-block:: python

    Traceback (most recent call last):
      File "tests.py", line 17, in <module>
        class Alg(AlgSign, AlgEnc):
      File "/v16/local/lib/python2.7/site-packages/enum/__init__.py", line 154, in __new__
        member_type, first_enum = metacls._get_mixins_(bases)
      File "/v16/local/lib/python2.7/site-packages/enum/__init__.py", line 469, in _get_mixins_
        raise TypeError("Cannot extend enumerations")
    TypeError: Cannot extend enumerations
    

ちょっと工夫

.. code-block:: python

    Signers = dict(
        RS256='RS256',
        RS512='RS512',
    )
    
    Encryptors = dict(
        A128KW='A128KW',
        A192KW='A192KW',
    )
    
    
    class AlgorithmBase(Enum):
        @property
        def is_signer(self):
            return Signers.get(self.value, None) is not None
    
        @property
        def is_encryptor(self):
            return Encryptors.get(self.value, None) is not None
    
        def __eq__(self, other):
            if isinstance(other, AlgorithmBase):
                return self.value == other.value
            return NotImplemented
    
        def __ne__(self, other):
            result = self.__eq__(other)
            if result is NotImplemented:
                return result
            return not result
    
    SignerEnum = type('SignersEnum', (AlgorithmBase, ), Signers)
    EncryptorEnum = type('EncryptorsEnum', (AlgorithmBase, ), Encryptors)
    
    #: AlgorithmEnum = SignerEnum + EncryptorEnum
    AlgorithmEnum = type('AlgorithmEnum', (AlgorithmBase, ),
                         dict(Signers, **Encryptors))
    
    #: テスト
    
    a1 = AlgorithmEnum('RS256')
    a2 = AlgorithmEnum('A128KW')
    
    assert a1.is_signer and a2.is_encryptor
    assert a1 == AlgorithmEnum.RS256 and a1 == SignerEnum.RS256
    assert a2 == AlgorithmEnum.A128KW and a2 == EncryptorEnum.A128KW
    
