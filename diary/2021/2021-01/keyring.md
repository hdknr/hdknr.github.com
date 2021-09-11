
https://github.com/pschmitt/python-keyring-lib-keyring

## Mac 

インストール:

~~~zsh
% pip install keyring

Collecting keyring
    Downloading keyring-21.8.0-py3-none-any.whl (32 kB)
Installing collected packages: keyring
Successfully installed keyring-21.8.0
~~~
    
使ってみる:
    
```py
In [1]: import keyring

In [2]: dir(keyring)
Out[2]: 
['__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 'backend',
 'backends',
 'core',
 'credentials',
 'delete_password',
 'errors',
 'get_credential',
 'get_keyring',
 'get_password',
 'set_keyring',
 'set_password',
 'util']
```
    
Macで使えるバックエンド:

```py
In [3]: keyring.backend.get_all_keyring()
Out[3]: 
[<keyring.backends.fail.Keyring at 0x1058b6a00>,
 <keyring.backends.chainer.ChainerBackend at 0x1058b6640>,
 <keyring.backends.OS_X.Keyring at 0x105817280>]
```
    
デフォルトでmacOSのキーチェーン:

```py
In [4]: keyring.get_keyring()
Out[4]: <keyring.backends.OS_X.Keyring at 0x105817280>

In [5]: keyring.set_password('service','user','password')

In [6]: keyring.get_password('service','user')
Out[6]: 'password'
```

### キーチェーンアクセス

アプリケーション -> ユーティリティ -> キーチェーンアクセスを開いてログイン項目として「service」を確認できる。

### securityコマンド

securityコマンドで確認可能

~~~zsh
% which security
    /usr/bin/security
    
% security find-generic-password -a user -s service -g

keychain: "/Users/hdknr/Library/Keychains/login.keychain-db"
version: 512
class: "genp"
attributes:
    0x00000007 <blob>="service"
    0x00000008 <blob>=<NULL>
    "acct"<blob>="user"
    "cdat"<timedate>=0x32303231303130333030343134315A00  "20210103004141Z\000"
    "crtr"<uint32>="aapl"
    "cusi"<sint32>=<NULL>
    "desc"<blob>=<NULL>
    "gena"<blob>=<NULL>
    "icmt"<blob>=<NULL>
    "invi"<sint32>=<NULL>
    "mdat"<timedate>=0x32303231303130333030343134315A00  "20210103004141Z\000"
    "nega"<sint32>=<NULL>
    "prot"<blob>=<NULL>
    "scrp"<sint32>=<NULL>
    "svce"<blob>="service"
    "type"<uint32>=<NULL>
password: "password"
~~~

## Debian

同じくpipでインストール。 

~~~bash
$ pip install keyring

Collecting keyring
  Downloading keyring-21.8.0-py3-none-any.whl (32 kB)
Collecting jeepney>=0.4.2
  Downloading jeepney-0.6.0-py3-none-any.whl (45 kB)
     |████████████████████████████████| 45 kB 9.1 MB/s 
Collecting SecretStorage>=3.2
  Downloading SecretStorage-3.3.0-py3-none-any.whl (14 kB)
Collecting cryptography>=2.0
  Downloading cryptography-3.3.1-cp36-abi3-manylinux2010_x86_64.whl (2.6 MB)
     |████████████████████████████████| 2.6 MB 19.4 MB/s 
Collecting cffi>=1.12
  Downloading cffi-1.14.4-cp39-cp39-manylinux1_x86_64.whl (405 kB)
     |████████████████████████████████| 405 kB 19.3 MB/s 
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 24.1 MB/s 
Collecting six>=1.4.1
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: pycparser, six, cffi, jeepney, cryptography, SecretStorage, keyring
Successfully installed SecretStorage-3.3.0 cffi-1.14.4 cryptography-3.3.1 jeepney-0.6.0 keyring-21.8.0 pycparser-2.20 six-1.15.0
~~~

~~~py
In [1]: import keyring

In [2]: keyring.backend.get_all_keyring()
Out[2]: 
[<keyring.backends.fail.Keyring at 0x7ff753fdaee0>,
 <keyring.backends.chainer.ChainerBackend at 0x7ff753f87760>]
~~~

~~~py
In [1]: import keyring

In [2]: keyring.get_keyring(        )
Out[2]: <keyring.backends.fail.Keyring at 0x7fabf5370be0>
~~~

- [ChainerBackend](https://github.com/jaraco/keyring/blob/main/keyring/backends/chainer.py) でバックエンドをリゾルブする 
- 設定がないので、[デフォルトバックエンドは失敗](https://github.com/jaraco/keyring/blob/main/keyring/backends/fail.py)

~~~py
>>> import keyring
>>> keyring.set_password('service','user1','password1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/vagrant/.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages/keyring/core.py", line 60, in set_password
    get_keyring().set_password(service_name, username, password)
  File "/home/vagrant/.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages/keyring/backends/fail.py", line 25, in get_password
    raise NoKeyringError(msg)
keyring.errors.NoKeyringError: No recommended backend was available. Install a recommended 3rd party backend package; or, install the keyrings.alt package if you want to use the non-recommended backends. See https://pypi.org/project/keyring for details.
~~~

### keyrings.cryptfile

- https://github.com/frispete/keyrings.cryptfile
- pycryptodome(PyCrypto互換) を使ってます

~~~bash
$ pip install keyrings.cryptfile
Collecting keyrings.cryptfile
  Downloading keyrings.cryptfile-1.3.6.tar.gz (18 kB)
Requirement already satisfied: keyring>=19.0.0 in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from keyrings.cryptfile) (21.8.0)
Requirement already satisfied: SecretStorage>=3.2 in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from keyring>=19.0.0->keyrings.cryptfile) (3.3.0)
Requirement already satisfied: jeepney>=0.4.2 in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from keyring>=19.0.0->keyrings.cryptfile) (0.6.0)
Requirement already satisfied: cryptography>=2.0 in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from SecretStorage>=3.2->keyring>=19.0.0->keyrings.cryptfile) (3.3.1)
Requirement already satisfied: six>=1.4.1 in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from cryptography>=2.0->SecretStorage>=3.2->keyring>=19.0.0->keyrings.cryptfile) (1.15.0)
Requirement already satisfied: cffi>=1.12 in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from cryptography>=2.0->SecretStorage>=3.2->keyring>=19.0.0->keyrings.cryptfile) (1.14.4)
Requirement already satisfied: pycparser in ./.anyenv/envs/pyenv/versions/3.9.0/lib/python3.9/site-packages (from cffi>=1.12->cryptography>=2.0->SecretStorage>=3.2->keyring>=19.0.0->keyrings.cryptfile) (2.20)
Collecting argon2_cffi
  Downloading argon2_cffi-20.1.0-cp35-abi3-manylinux1_x86_64.whl (97 kB)
     |████████████████████████████████| 97 kB 9.5 MB/s 
Collecting pycryptodome
  Downloading pycryptodome-3.9.9-cp39-cp39-manylinux1_x86_64.whl (13.7 MB)
     |████████████████████████████████| 13.7 MB 9.8 MB/s 
Using legacy 'setup.py install' for keyrings.cryptfile, since package 'wheel' is not installed.
Installing collected packages: pycryptodome, argon2-cffi, keyrings.cryptfile
    Running setup.py install for keyrings.cryptfile ... done
Successfully installed argon2-cffi-20.1.0 keyrings.cryptfile-1.3.6 pycryptodome-3.9.9

~~~

~~~py
In [1]: import keyring

In [2]: keyring.backend.get_all_keyring()
Out[2]: 
[<keyring.backends.fail.Keyring at 0x7f520eb48490>,
 <EncryptedKeyring with [PBKDF2] AES256.CFB v.1.0 at /home/vagrant/.local/share/python_keyring/crypted_pass.cfg>,
 <keyring.backends.chainer.ChainerBackend at 0x7f520ead1f40>,
 <PlaintextKeyring with no encyption v.1.0 at /home/vagrant/.local/share/python_keyring/keyring_pass.cfg>,
 <CryptFileKeyring with [Argon2] AES128.GCM v.1.3.6 at /home/vagrant/.local/share/python_keyring/cryptfile_pass.cfg>]
~~~


~~~py
In [3]: keyring.get_keyring()
Out[3]: <keyring.backends.chainer.ChainerBackend at 0x7f56a8a4afd0>

In [4]: keyring.set_password('service','user1','password1')
Please set a password for your new keyring: master1 
Please confirm the password:  master1
~~~

~~~bash
$ tree ~/.local/
/home/vagrant/.local/
└── share
    ├── composer
    └── python_keyring
        └── cryptfile_pass.cfg
~~~

~~~bash
$ more ~/.local/share/python_keyring/cryptfile_pass.cfg 
[[keyring_2Dsetting]
password_20reference = 
        eyJzYWx0IjogIjVQMGtKdmZLZExacVN3UEN2ZVNrS0E9PSIsICJkYXRhIjogIjJkMS9WVjIwRjRl
        eG5EV3FnVEJmeTVVVXFNaC9kazduIiwgIm1hYyI6ICJncVVjVmlBbW1WcmdROW9tM1UrcTdRPT0i
        LCAibm9uY2UiOiAiaXcyZGp3ZkVBdmlId2pGSEZBaWMydz09In0=
scheme = [Argon2] AES128.GCM
version = 1.3.6

[service]
user = 
        eyJzYWx0IjogIkl0TXRlTFJMYUp3R2pWdmp6aVpzRHc9PSIsICJkYXRhIjogIndsV21CV2NhWlNu
        cyIsICJtYWMiOiAici9ZcEtlYkh2LzUvenFpSXRtdFpaZz09IiwgIm5vbmNlIjogInRldG1FUHp0
        S2dYVG10ajV4UVVXWkE9PSJ9

~~~


## Json Base64したもの ##

[keyring_2Dsetting]セクション

~~~py
In [1]: keydata = '''
   ...:         eyJzYWx0IjogImx3QWgxbUNFU2RsTkx4d2NNaWNOMEE9PSIsICJkYXRhIjogInZhd0ZnNWxXNWRG
   ...:         c0dhTkdyZXF6aEpxTnlwSmZnR1VGIiwgIm1hYyI6ICIzaTlQL2ZqVEJFT29qMHZ6YUxlM2VRPT0i
   ...:         LCAibm9uY2UiOiAiZnlTVGpxaWsxL0dnOUxGNTA2MmI1UT09In0=
   ...: '''    

In [2]: import base64, json

In [3]: key_param = json.loads(base64.b64decode(keydata.replace(' ', '').replace('\n', '')))

In [4]: key_param
Out[4]: 
{'salt': 'lwAh1mCESdlNLxwcMicN0A==',
 'data': 'vawFg5lW5dFsGaNGreqzhJqNypJfgGUF',
 'mac': '3i9P/fjTBEOoj0vzaLe3eQ==',
 'nonce': 'fySTjqik1/Gg9LF5062b5Q=='}
~~~


```py
    >>> key_data = '''eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiazloc1R1bmt3UERnRGo0TFY3UWljcVQybGxoSTRJS3Ns
    ...     Z1BVXG4iLCAic2FsdCI6ICJrcUZYUWhTMkR1ZEZGMjFkK3BpRmVJbll5dVkzY3V4MWlyam5OT3Zt
    ...     azBFPVxuIiwgIklWIjogIkQ0YUhEQ1VJbVhTUnFLZmN4MXRicmc9PVxuIn0='''.replace(' ','').replace('\n','')
    
    >>> import base64
    >>> import json
    >>> key_param = json.loads(base64.decodestring(key_data))
    >>> key_param
    {u'salt': u'kqFXQhS2DudFF21d+piFeInYyuY3cux1irjnNOvmk0E=\n', 
     u'password_encrypted': u'k9hsTunkwPDgDj4LV7QicqT2llhI4IKslgPU\n', 
     u'IV': u'D4aHDCUImXSRqKfcx1tbrg==\n'}
    
    >>> lambda d: dict([ (base64.decodestring(k.encode()), base64.decodestring(v.encode())) for k,v in d.items()])
    <function <lambda> at 0x7f4aba18dd70>
    >>> cv = _
    >>> key_param = cv(key_param)
    >>> key_param
    {'password_encrypted': '\x93\xd8lN\xe9\xe4\xc0\xf0\xe0\x0e>\x0bW\xb4"r\xa4\xf6\x96XH\xe0\x82\xac\x96\x03\xd4', 
     'salt': '\x92\xa1WB\x14\xb6\x0e\xe7E\x17m]\xfa\x98\x85x\x89\xd8\xca\xe67r\xecu\x8a\xb8\xe74\xeb\xe6\x93A', 
      'IV': '\x0f\x86\x87\x0c%\x08\x99t\x91\xa8\xa7\xdc\xc7[[\xae'}
```

## pycrypto & AES CBF ##

[pycrypto](https://www.dlitz.net/software/pycrypto/)があれば使います。
blockサイズ32で [CFBブロック暗号化](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)。
saltを使って[キーを派生させます](https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.Protocol.KDF-module.html)

```py

    >>> from Crypto.Protocol.KDF import PBKDF2
    >>> from Crypto.Cipher import AES
    >>> pw_key = PBKDF2('root', key_param['salt'], 32)
    >>> cipher_key = AES.new(pw_key[:32], AES.MODE_CFB, key_param['IV'])
    >>> keyring_password = cipher_key.decrypt(key_param['password_encrypted']).decode('utf8')
    >>> keyring_password
    u'pw:password reference value'
    
    プレフィックス除く
    >>> p = keyring_password[3:]
    >>> p
    u'password reference value'
```

同じくユーザーデータ

```py
    >>> user_data ='''eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiY1VNVERaT1F4YWh4SElvPVxuIiwgInNhbHQiOiAicTg3
    ...     L0hDcmVOYTk1blBydFlvZVl4czB6aEVlSzVxMWdFTnUvdGtKRUhtYz1cbiIsICJJViI6ICI1TU5G
    ...     RjBZbnZzdyt2elFabWNTNmF3PT1cbiJ9'''.replace(' ','').replace('\n','')
    
    >>> user_param = cv( json.loads( base64.decodestring(user_data) ) )
    >>> user_param
    {'password_encrypted': 'qC\x13\r\x93\x90\xc5\xa8q\x1c\x8a', 'salt': '\xab\xce\xff\x1c*\xde5\xafy\x9c\xfa\xedb\x87\x98\xc6\xcd3\x84G\x8a\xe6\xad`\x10\xdb\xbf\xb6BD\x1eg', 'IV': "\xe4\xc3E\x17F'\xbe\xcc>\xbf4\x19\x99\xc4\xbak"}
    
    
    >>> pw_user = PBKDF2('root', user_param['salt'], 32)
    >>> cipher_user = AES.new(pw_user[:32], AES.MODE_CFB, user_param['IV'])
    >>> cipher_user.decrypt(user_param['password_encrypted']).decode('utf8')[3:]
    u'password'
```
