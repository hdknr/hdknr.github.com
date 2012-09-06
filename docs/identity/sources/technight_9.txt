==========================================
Technight #9
==========================================

.. contents::

Cloud Identity Summit '12 TOI
==========================================

- 工藤達夫

内容
----

- CIS '12 TOI(Transafer of Information )
- Workshop,Sessionsからのネタ

What?
-------

- cloudidentitysummit.com
- 3回目

- Jul 16, OIDF
- Jul 17, OIX
- Jul 18, ガバナンス、ガバメント, Edge Cases(先進事例)
  CSA,Enterpise,アナリスト観点
- Jul 19, API, mobie, 世界事例
  堤防,WSIFT,社会正義

Identitiy is the New Perimeter
--------------------------------------------

- 外周、境界 : 意味ないんじゃないの
- ユーザー x デバイス 増える一方
- ファイウォールの「向こう側」をどうやって守るか？

外部化
------

- サービス、データ、ユーザー、アセット
- 堤防が意味ない、決壊している

アイデンティティはセキュリティのおまけ「ではない」
------------------------------------------------------------------

- Identity & Security

APIに求められる「トラスト」:アイデンティティが境界
-------------------------------------------------------

- ユーザーアイデンティティをもとにアクセス管理

トラストモデル：多極分散へ
------------------------------------------------

SAML is Dead.
----------------------------------------

- みんなSAML好き

ほんとに死んだの？
----------------------------------------

- 今からやらないよね。
- Web SSO が置き換えられつつある。

Connect 注目
----------------------------------------

- SAML + OAuth から Connectはそろそろどうかな？

Connect:OAuth 2.0に置けるアイデンティティのデザインパターン
------------------------------------------------------------------

- 系図  
- 簡単につかえるし、難しい事もできるよ

デモ:  福家(ふけ)さん Ping Identity
------------------------------------------------------------

- Elevator Pitch

    - Identity Layer over OAuth 2
    
- Differentiators

    - OpenID 2.0

        - Dicovery Simpler
        - LoA

    -  SAML

        - Simpler Assertion : JSON
        - Web + Native Application

    - OAuth 2 
        
        - Identity
        - Encryption
        - TLS

- Spec Family

- デモ : Patrick Harding @ CIS2012

    - O/L Stock Trading
    - Stock Export , idTrade

Connect: なぜ？
-------------------------------------------------------

- B2C/B2Bをともにカバー
- SSO
- API認可
- Webっぽい (JSONとかRESTとか。。。)
- Discoveryがよくなった
- ベンダーが多くなった

    - Gluu, IBM,Layer7, MS, NRI, Ping, Vordel   
    - ..

Paypal Access : Connect対応
------------------------------------

- Connect プロダクションバージョン
- OAuth 2 , Still Beta
- レガシープロトコルとかがたくさんあるが、 OAuth2/Connectに統一して行く(雑談)
- ConnectだけではなくてSAMLも使うよ 
- 過渡期( Connectに行きつつあるが、SAMLもあるよ )

Google
---------------------------------

- accountchooser.com

    - HTML 5 local storage に書き込む
    - ac.js で簡単にできる
    - SSO
    - google.comに組み込む予定 : エンドユーザーが知らないうちに使えるようになって行く
    - サーチエンジンに組み込み:ac対応のRPのレートが上がる

- Identity Verification
 
    - "Street Identity" 
    - Attribute Exchange APIのパイロット
    - "oauthgoog" で検索してよ

Mobile:Security + Identity
------------------------------

- Identityの考慮がこれから需要

アクセス権のレボケーション
------------------------------

- Mobileでは難しかったりする
- これから重要

BYOD + IdM
------------------------------

- "Stak View"

ライトニングトーク vol.9 (IDCフロンティア山下)
============================================================

Service Concept
--------------------

- RightScale
- OpenStack

きっかけ
---------------

- 複数のID/PWDの管理
- OpenIDでID統合やるのはどうかな     
- おもしろそうだった

Enterprise & Connect
--------------------------------------------

- オンプレ -- (Connect)-- クラウド
- Citrix XenDesktopにAccount Chooser いれたいな
- CSAクラウドコンピューティングのためのセキュリティガイダンス

IIJグローバルソリューソンズ : 竹内さん
=======================================================

Pingの代理店
----------------

- 2012/04
- JP & Asia
- Ping Federate
- クラウド認証連携ソリューション

Keyword
--------------------

- SAML -> Connect
- BYOD
- SCIM (スキム )
- IDaaS (アイダース)

GIO
-----

- クラウドサービス"GIO"


tkudo
==========

- Connectやんないとなー。
- "SAML is dead"

Cambrian Explosion of Everything
------------------------------------

- Explosion of API, Nodes, Data, Time, Mobile, Decentralization

URL
-------
