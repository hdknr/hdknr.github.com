#!/bin/bash

COMMAND="curl -O"
mkdir -p specs
cd specs

# OAuth
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-v2-30
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-assertions-04
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-v2-threatmodel-06
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-v2-bearer-22
$COMMAND http://tools.ietf.org/html/draft-jones-oauth-jwt-bearer-04
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-saml2-bearer-13
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-v2-http-mac-01
$COMMAND http://tools.ietf.org/html/draft-oauth-dyn-reg-v1-03
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-revocation-00

#Connect
$COMMAND http://openid.bitbucket.org/openid-connect-basic-1_0.html
$COMMAND http://openid.bitbucket.org/openid-connect-implicit-1_0.html
$COMMAND http://openid.bitbucket.org/openid-connect-standard-1_0.html 
$COMMAND http://openid.bitbucket.org/openid-connect-messages-1_0.html
$COMMAND http://openid.bitbucket.org/openid-connect-discovery-1_0.html
$COMMAND http://openid.bitbucket.org/openid-connect-registration-1_0.html
$COMMAND http://openid.bitbucket.org/openid-connect-session-1_0.html
$COMMAND http://openid.bitbucket.org/oauth-v2-multiple-response-types-1_0.html

#UMA
$COMMAND http://tools.ietf.org/html/draft-hardjono-oauth-umacore-04

#JOSE
$COMMAND http://tools.ietf.org/html/draft-ietf-oauth-json-web-token-02
$COMMAND http://tools.ietf.org/html/draft-ietf-jose-json-web-signature-04
$COMMAND http://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-04
$COMMAND http://tools.ietf.org/html/draft-ietf-jose-json-web-key-04
$COMMAND http://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-04
$COMMAND http://tools.ietf.org/html/draft-jones-json-web-signature-json-serialization-02
$COMMAND http://tools.ietf.org/html/draft-jones-json-web-encryption-json-serialization-02
$COMMAND http://tools.ietf.org/html/draft-barnes-jose-use-cases-00
$COMMAND http://tools.ietf.org/html/draft-barnes-jose-jsms-00
$COMMAND http://tools.ietf.org/html/draft-manger-jose-jwsec-00
$COMMAND http://tools.ietf.org/html/draft-schaad-jose-serialize-00

