# -*- coding: utf-8 -*-

'''
    >>> text =open("data.txt").read()
    >>> print "[%s]" % text
    >>> key_file="server.ecdsa.key"
    >>> key = load_key(open(key_file).read())
    >>> x509_file="server.ecdsa.pem.crt"
    >>> pub = load_pub_key(open(x509_file).read())
    >>> 
    >>> #: 署名の作成
    >>> sig,digest = ec_sha1_sign_asn1(key,text)
    >>> 
    >>> print "digest=",len(digest),binascii.hexlify(digest)
    >>> print "signature =",len(sig),binascii.hexlify(sig)
    >>> print "signature(base64) =",len(sig),base64.b64encode(sig)
    >>> 
    >>> #: 検証
    >>> print pub.verify_dsa_asn1(digest,sig)
'''

def ec_sha1_sign_asn1(pri,text):
    ''' プライベートキーで署名をASN.1 Objectで作成します。
    '''
    digest=hashlib.sha1(text).digest()
    signature  = key.sign_dsa_asn1(digest)
    return signature,digest 

def ec_sha1_verify_asn1(ASpub,text,signature):
    ''' パブリックキーでASN.1 Object形式の署名を検証します。
    '''
    digest=hashlib.sha1(text).digest()
    return 1 == pub.verify_dsa_asn1(digest,siganture)


def load_key(pem):
    ''' PEM形式のECプライベートキーを読み込みます '''
    from M2Crypto import EC,BIO
    bio = BIO.IOBuffer( BIO.MemoryBuffer(pem) )
    key = EC.load_key_bio(bio) 
    return key 

def load_pub_key(pem_x509):
    ''' PEM形式のX.509 証明書から、ECパブリックキーを取得します'''
    from M2Crypto import X509
    from M2Crypto import EC
    x509 = X509.load_cert_string(pem_x509)
    return EC.pub_key_from_der(x509.get_pubkey().as_der() )

