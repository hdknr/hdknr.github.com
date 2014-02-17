=======================================
Active Directory
=======================================

.. contents:: AD
    :local:        

- :doc:`windows`

Install
=========

- `Windows Server 2008 R2 にインストール <http://note.harajuku-tech.org/windows-2008-active-directory>`_

-  `Active Directory DSのインストールとDCへの昇格 <https://www.evernote.com/shard/s302/sh/bb818d0d-b0e5-4920-b5bf-6d69ba32d511/66a628ad1b32d3acfe74a9011f4880ec>`_

- `メンバーサーバーとしてドメイン参加 <https://www.evernote.com/shard/s302/sh/dc85a41c-b4ba-4278-8ab1-458b401808eb/c796140ac8f73b202543dd944b35dfe0>`_


Active Directory & Connect
==================================

Clientも同一ドメインの場合
------------------------------------------

- Client(RP) のトークンリクエストもドメイン認証可能
                  
Clientがドメイン外部の場合
------------------------------------------

- NT Domain は Outsideの接続を許可する必要有り(FirewallやVPNなど)
- クライアントクレデンシャルをRegist する必要あり(通常のConnect)

Serverが別途ありドメイン内部の場合
------------------------------------------

- ServerがUMAのトークンステータス確認の為の接続をドメイン認証でできる

                  
Serverが別途ありドメイン外部の場合
------------------------------------------

- ServerがUMAのトークンステータス確認接続の為に外部から接続を許可する必要あり
    - トークンステータスを事前(Clientにトークン/コードを返前)に 
      OP(AM) -> Serverに送信するプロファイルがUMAにあれば、Serverはレジストレーションで
      信頼関係(アソシエーション）だけ作っておけばinboudリクエスト入らないかも。

- Server(UMA Host)とADとの間で関係づけする時にはinboudの接続は必要か。



dsquery コマンド
===================================

::

    C:\> dsquery user -name Administrator

    "CN=Administrator,CN=Users,DC=win,DC=hdknr,DC=info"

Userの取得
===========

.. code-block:: csharp

    using System.DirectoryServices;

    // cname : Active Directory ドメインのコモンネーム( www.microsoft.com など) 
    private static DirectoryEntry FindUser(string username, string cname)
    {
        string path = "CN=" + username + ",CN=Users";
        foreach (var i in cname.Split('.'))
        {
            path += ",DC=" + i;
        }
        return  new DirectoryEntry("LDAP://" + path);
    }

ユーザ−属性の取得
====================

.. code-block:: csharp

    // 辞書で返す
    public static object GetProperties(string username, string cname)
    {
        Dictionary<string, string> ret = new Dictionary<string, string>();
        foreach (PropertyValueCollection prop in User.FindUser(username, cname).Properties)
        {
            ret[prop.PropertyName] = prop.Value.ToString();
        }
        return ret; // ;
    }
       
.. code-block:: javascript

    {
      "primaryGroupID": "513", 
      "isCriticalSystemObject": "True", 
      "logonCount": "71", 
      "cn": "Administrator", 
      "countryCode": "0", 
      "dSCorePropagationData": "System.Object[]", 
      "objectClass": "System.Object[]", 
      "adminCount": "1", 
      "lastLogonTimestamp": "System.__ComObject", 
      "instanceType": "4", 
      "sAMAccountName": "Administrator", 
      "distinguishedName": "CN=Administrator,CN=Users,DC=win,DC=hdknr,DC=info", 
      "sAMAccountType": "805306368", 
      "lastLogoff": "System.__ComObject", 
      "logonHours": "System.Byte[]", 
      "objectSid": "System.Byte[]", 
      "whenCreated": "2012/04/10 19:26:27", 
      "uSNCreated": "System.__ComObject", 
      "mail": "administrator@win.hdknr.info", 
      "badPasswordTime": "System.__ComObject", 
      "pwdLastSet": "System.__ComObject", 
      "nTSecurityDescriptor": "System.__ComObject", 
      "description": "コンピューター/ドメインの管理用 (ビルトイン アカウント)", 
      "objectCategory": "CN=Person,CN=Schema,CN=Configuration,DC=win,DC=hdknr,DC=info", 
      "objectGUID": "System.Byte[]", 
      "whenChanged": "2012/04/16 5:18:35", 
      "uSNCreated": "System.__ComObject", 
      "mail": "administrator@win.hdknr.info", 
      "badPasswordTime": "System.__ComObject", 
      "pwdLastSet": "System.__ComObject", 
      "nTSecurityDescriptor": "System.__ComObject", 
      "description": "コンピューター/ドメインの管理用 (ビルトイン アカウント)", 
      "objectCategory": "CN=Person,CN=Schema,CN=Configuration,DC=win,DC=hdknr,DC=info", 
      "objectGUID": "System.Byte[]", 
      "whenChanged": "2012/04/16 5:18:35", 
      "badPwdCount": "0", 
      "accountExpires": "System.__ComObject", 
      "displayName": "管理者さん", 
      "telephoneNumber": "+81+3-3333-3333", 
      "wWWHomePage": "http://win.hdknr.info/user/administrator", 
      "physicalDeliveryOfficeName": "雲", 
      "name": "Administrator", 
      "memberOf": "System.Object[]", 
      "codePage": "0", 
      "userAccountControl": "512", 
      "lastLogon": "System.__ComObject", 
      "uSNChanged": "System.__ComObject", 
      "sn": "偉", 
      "servicePrincipalName": "MSSQLSvc/AMAZONA-4U921BK.win.hdknr.info:SQLEXPRESS", 
      "givenName": "人", 
      "initials": "admin"
    }


