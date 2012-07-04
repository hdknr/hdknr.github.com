================================================
s_client : SSL/TLS client program
================================================


.. contents:: s_client

s_client
==============

mail.google.com を見てみる
------------------------------------------

::

    $ openssl s_client -connect mail.google.com:443  > mail.google.com.txt

    depth=1 /C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
    verify error:num=20:unable to get local issuer certificate
    verify return:0

    (^D)

    DONE

以下、 mail.google.com.txt の内容

::

    CONNECTED(00000003)
    ---

::

    Certificate chain
     0 s:/C=US/ST=California/L=Mountain View/O=Google Inc/CN=mail.google.com
       i:/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
     1 s:/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
       i:/C=US/O=VeriSign, Inc./OU=Class 3 Public Primary Certification Authority
    ---

::

    Server certificate
    -----BEGIN CERTIFICATE-----
    MIIDIjCCAougAwIBAgIQK59+5colpiUUIEeCdTqbuTANBgkqhkiG9w0BAQUFADBM
    MQswCQYDVQQGEwJaQTElMCMGA1UEChMcVGhhd3RlIENvbnN1bHRpbmcgKFB0eSkg
    THRkLjEWMBQGA1UEAxMNVGhhd3RlIFNHQyBDQTAeFw0xMTEwMjYwMDAwMDBaFw0x
    MzA5MzAyMzU5NTlaMGkxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlh
    MRYwFAYDVQQHFA1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKFApHb29nbGUgSW5jMRgw
    FgYDVQQDFA9tYWlsLmdvb2dsZS5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJ
    AoGBAK85FZho5JL+T0/xu/8NLrD+Jaq9aARnJ+psQ0ynbcvIj36B7ocmJRASVDOe
    qj2bj46Ss0sB4/lKKcMP/ay300yXKT9pVc9wgwSvLgRudNYPFwn+niAkJOPHaJys
    Eb2S5LIbCfICMrtVGy0WXzASI+JMSo3C2j/huL/3OrGGvvDFAgMBAAGjgecwgeQw
    DAYDVR0TAQH/BAIwADA2BgNVHR8ELzAtMCugKaAnhiVodHRwOi8vY3JsLnRoYXd0
    ZS5jb20vVGhhd3RlU0dDQ0EuY3JsMCgGA1UdJQQhMB8GCCsGAQUFBwMBBggrBgEF
    BQcDAgYJYIZIAYb4QgQBMHIGCCsGAQUFBwEBBGYwZDAiBggrBgEFBQcwAYYWaHR0
    cDovL29jc3AudGhhd3RlLmNvbTA+BggrBgEFBQcwAoYyaHR0cDovL3d3dy50aGF3
    dGUuY29tL3JlcG9zaXRvcnkvVGhhd3RlX1NHQ19DQS5jcnQwDQYJKoZIhvcNAQEF
    BQADgYEANYARzVI+hCn7wSjhIOUCj19xZVgdYnJXPOZeJWHTy60i+NiBpOf0rnzZ
    wW2qkw1iB5/yZ0eZNDNPPQJ09IHWOAgh6OKh+gVBnJzJ+fPIo+4NpddQVF4vfXm3
    fgp8tuIsqK7+lNfNFjBxBKqeecPStiSnJavwSI4vw6e7UN0Pz7A=
    -----END CERTIFICATE-----
    subject=/C=US/ST=California/L=Mountain View/O=Google Inc/CN=mail.google.com
    issuer=/C=ZA/O=Thawte Consulting (Pty) Ltd./CN=Thawte SGC CA
    ---

::

    No client certificate CA names sent
    ---

::

    SSL handshake has read 1773 bytes and written 316 bytes
    ---

::

    New, TLSv1/SSLv3, Cipher is RC4-SHA
    Server public key is 1024 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    SSL-Session:
        Protocol  : TLSv1
        Cipher    : RC4-SHA
        Session-ID: E27604298D3C8AA2EC97E47945024200C66A653D29EA9B33F23BFF06B5AFEBDF
        Session-ID-ctx: 
        Master-Key: EF45B6AE4DDB3BA2679EBFABBAC2DE3D7DE3470497654FBB4E681B6774E95933AC1AC482799B1E0B55B54C9991E139C9
        Key-Arg   : None
        Start Time: 1341297633
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)
    ---
    
www.apple.comの全ての証明書を見てみる
---------------------------------------------


::

    openssl s_client -showcerts -connect www.apple.com:443 > www.apple.com.txt

::

    depth=1 /C=US/O=Akamai Technologies Inc/CN=Akamai Subordinate CA 3
    verify error:num=20:unable to get local issuer certificate
    verify return:0
    (^D)
    DONE
    

以下 www.apple.com.txt

::

    CONNECTED(00000003)
    ---

::

    Certificate chain
     0 s:/C=US/L=Cupertino/O=Apple Inc./ST=CALIFORNIA/CN=www.apple.com
       i:/C=US/O=Akamai Technologies Inc/CN=Akamai Subordinate CA 3
    -----BEGIN CERTIFICATE-----
    MIIDJzCCApCgAwIBAgIOAQAAAAABNwl6mQWT01EwDQYJKoZIhvcNAQEFBQAwUTEL
    MAkGA1UEBhMCVVMxIDAeBgNVBAoTF0FrYW1haSBUZWNobm9sb2dpZXMgSW5jMSAw
    HgYDVQQDExdBa2FtYWkgU3Vib3JkaW5hdGUgQ0EgMzAeFw0xMjA1MDExNzUzNDNa
    Fw0xMzA1MDExNzUzNDNaMGMxCzAJBgNVBAYTAlVTMRIwEAYDVQQHEwlDdXBlcnRp
    bm8xEzARBgNVBAoTCkFwcGxlIEluYy4xEzARBgNVBAgTCkNBTElGT1JOSUExFjAU
    BgNVBAMTDXd3dy5hcHBsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
    AoIBAQCdJlExG8umAtxL9Df/10diaYoqFeeVDbU13cH0KNxq2vV0nSb3dROtUAig
    /wXj6jFU16fhfFegjcYBkYL9qiUkIiROMNo9r1IzZX4Yv9HT30vBdRMZkuIdy9eP
    m9nctNVYyBGRJapem1c+llxAJzToiuQofBY6L6K2dO7nuGm7AZ/PwcbyxZEWoh0E
    2SKMbMD9vG0Dph+rZDcPxENFa401j95ZiyyDinHXPliPVGimQmLeaWXMOhJSGXcd
    FidodxJCGPUIMuQnxipIH8EAiOg76aKsFvi/7ctoYtRGsXJZqRLnKJ2JVAq+tQxj
    6so8vaO5I5wqjyCa+ECJJ0i8Vhp/AgMBAAGjbDBqMDkGA1UdHwQyMDAwLqAsoCqG
    KGh0dHA6Ly9jcmwuZ2xvYmFsc2lnbi5uZXQvQWthbWFpU3ViMy5jcmwwHQYDVR0O
    BBYEFK5QfqCwo5h4aWa7DmhIJdMZ50FjMA4GA1UdDwEB/wQEAwIFIDANBgkqhkiG
    9w0BAQUFAAOBgQCMfDikw5AwrCCCkhcb+ak5oTRmhV88mL5Pk7SzVTbMdCoaktOD
    +Bu7iX0OYsISOjYu0x2CzX2VQ5kP5NhA7fqXOiq4iG1G/Ae+xW01lUB1gJ7VUwoX
    9LabdT6c812EOMpza4lrnLqnOsiSCDf1SWv0Lo+pMkZ9Ka9EbSd3DqUEHw==
    -----END CERTIFICATE-----
     1 s:/C=US/O=Akamai Technologies Inc/CN=Akamai Subordinate CA 3
       i:/C=US/O=GTE Corporation/OU=GTE CyberTrust Solutions, Inc./CN=GTE CyberTrust Global Root
    -----BEGIN CERTIFICATE-----
    MIIDxzCCAzCgAwIBAgIEBAAEAzANBgkqhkiG9w0BAQUFADB1MQswCQYDVQQGEwJV
    UzEYMBYGA1UEChMPR1RFIENvcnBvcmF0aW9uMScwJQYDVQQLEx5HVEUgQ3liZXJU
    cnVzdCBTb2x1dGlvbnMsIEluYy4xIzAhBgNVBAMTGkdURSBDeWJlclRydXN0IEds
    b2JhbCBSb290MB4XDTA2MDUxMTE1MzIwMFoXDTEzMDUxMTIzNTkwMFowUTELMAkG
    A1UEBhMCVVMxIDAeBgNVBAoTF0FrYW1haSBUZWNobm9sb2dpZXMgSW5jMSAwHgYD
    VQQDExdBa2FtYWkgU3Vib3JkaW5hdGUgQ0EgMzCBnzANBgkqhkiG9w0BAQEFAAOB
    jQAwgYkCgYEAnTR2c7MmRMRgzHZfj9gvSzoSVoxt1bTirAzhR4qFQxK8A2aFIB1r
    inRyOIVhqXMLV1vbxZ6zZsVR+AqQfPh0FHISgPToWs3IuxEUyUQv7OGvM8FZKd1M
    hXscgN1GpWTPYO9PVZM+BakWJCtI/58Fkt4M559g31Rvpxbu/69hqZ0CAwEAAaOC
    AYYwggGCMEUGA1UdHwQ+MDwwOqA4oDaGNGh0dHA6Ly93d3cucHVibGljLXRydXN0
    LmNvbS9jZ2ktYmluL0NSTC8yMDE4L2NkcC5jcmwwHQYDVR0OBBYEFL45v0Fm+tTO
    i254o0l+3j3ELiv2MFMGA1UdIARMMEowSAYJKwYBBAGxPgEAMDswOQYIKwYBBQUH
    AgEWLWh0dHA6Ly93d3cucHVibGljLXRydXN0LmNvbS9DUFMvT21uaVJvb3QuaHRt
    bDCBoAYDVR0jBIGYMIGVgBSmDB2fYf8HF7W/OEbbQzDVjrBSBqF5pHcwdTELMAkG
    A1UEBhMCVVMxGDAWBgNVBAoTD0dURSBDb3Jwb3JhdGlvbjEnMCUGA1UECxMeR1RF
    IEN5YmVyVHJ1c3QgU29sdXRpb25zLCBJbmMuMSMwIQYDVQQDExpHVEUgQ3liZXJU
    cnVzdCBHbG9iYWwgUm9vdIICAaUwDgYDVR0PAQH/BAQDAgHGMBIGA1UdEwEB/wQI
    MAYBAf8CAQAwDQYJKoZIhvcNAQEFBQADgYEAdofTrk09xGso4VIfeYEe6WIa90/Z
    GsDlBRH6d/n/sSUXXsoZyKzM3HGVzs9mAmDBfv/s2bZw4QNgM0MMNlWNMJddXZcJ
    bZ14M6VWhKYouKEZnaAsSCe+XHsF0haUfOnxpj4p7CZj/DnGZVB8Uh92ORa0lyY5
    q44d/bV6wDodO38=
    -----END CERTIFICATE-----
    ---

::

    Server certificate
    subject=/C=US/L=Cupertino/O=Apple Inc./ST=CALIFORNIA/CN=www.apple.com
    issuer=/C=US/O=Akamai Technologies Inc/CN=Akamai Subordinate CA 3
    ---

::

    No client certificate CA names sent
    ---

::

    SSL handshake has read 1954 bytes and written 456 bytes
    ---

::

    New, TLSv1/SSLv3, Cipher is AES256-SHA
    Server public key is 2048 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    SSL-Session:
        Protocol  : TLSv1
        Cipher    : AES256-SHA
        Session-ID: E305375AEFE48AF4A7CEE4BC503406499A7D3C5DF61AC650A915B2381CA9175C
        Session-ID-ctx: 
        Master-Key: 75BE8BC2F58C08FF7A7FDFC4B3BDEDD81E2B8C53CE0F7B9635388E3096AB9F877505B429BE97164725AEC7F491CFAFB8
        Key-Arg   : None
        Start Time: 1341297941
        Timeout   : 300 (sec)
        Verify return code: 0 (ok)
    ---
    


Python
======

sslモジュールでX.509証明書を取得
---------------------------------------------

ssl.get_server_certificate() でPEM形式のX.509証明書を取得可能

.. code-block:: python

    >>> import ssl
    >>> ssl.get_server_certificate(('mail.google.com',443))

    '-----BEGIN CERTIFICATE-----\nMII.....
    ......
    ....UN0Pz7A=\n-----END CERTIFICATE-----\n'


C#
=====

SslStreamとX509Certificate2でX.509証明書を取得
--------------------------------------------------

.. code-block:: csharp

    using System.Net.Sockets;
    using System.Net.Security;
    using System.Security.Cryptography.X509Certificates;
    

指定したCNAMEのSSLサーバーのX509Certificate2オブジェクトを取得する。

.. code-block:: csharp

        public static X509Certificate2  X509FromSsl(string serverName)
        {
            var client = new TcpClient(serverName, 443);

            // Create an SSL stream that will close the client's stream.
            using (var sslStream = new SslStream(client.GetStream(), true))
            {
                sslStream.AuthenticateAsClient(serverName);
                var serverCertificate = sslStream.RemoteCertificate;

                var managedCert = new X509Certificate2(serverCertificate);
                var chain = new X509Chain();
                chain.Build(managedCert);

                foreach (var element in chain.ChainElements)
                {
                    if (element.Certificate.SubjectName.Name.Contains(string.Format("CN={0}", serverName)))
                    {
                        return element.Certificate;
                    }
                }
            }
            return null;

        }
    
X509Certificate2 オブジェクトから :term:`DER` のバイナリストリームを取得し、Base64して :term:`PEM` 化する

.. code-block:: csharp

        public static string ToPem(X509Certificate2 certobj)
        {
            return ToPem( certobj.Export(X509ContentType.Cert ) );
        }

        public static string ToPem(byte[] der_bytes)
        {
            StringBuilder builder = new StringBuilder();
            builder.AppendLine("-----BEGIN CERTIFICATE-----");
            builder.AppendLine(Convert.ToBase64String(der_bytes,
                                0, der_bytes.Length,
                                Base64FormattingOptions.InsertLineBreaks));
            builder.AppendLine("-----END CERTIFICATE-----");
            return builder.ToString();

        }

