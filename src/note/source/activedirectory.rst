==================
Active Directory
==================

.. contents:: AD

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


