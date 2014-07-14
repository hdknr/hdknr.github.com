==========================================================================================
Active Directory Domain Controller インストール
==========================================================================================


.. contents::
    :local:


手順
======

インストール
---------------

サーバーマネージャダッシュボード起動

.. image:: ad_install/ad_install.1.png
    :scale: 50 %

次へ

.. image:: ad_install/ad_install.2.png
    :scale: 50 %

サーバー選択

.. image:: ad_install/ad_install.3.png
    :scale: 50 %

Active Directory ドメインサービス選択

.. image:: ad_install/ad_install.4.png
    :scale: 50 %

機能の追加

.. image:: ad_install/ad_install.5.png
    :scale: 50 %

選択されたので次へ

.. image:: ad_install/ad_install.6.png
    :scale: 50 %

インストールオプションの確認。次へ。

.. image:: ad_install/ad_install.7.png
    :scale: 50 %

Active Directory ドメインサービス。次へ。

.. image:: ad_install/ad_install.8.png
    :scale: 50 %

再度インストールオプション確認。インストール。

.. image:: ad_install/ad_install.9.png
    :scale: 50 %

インストールできた。ここで :ref:`「このサーバーをドメインコントーラに昇格」<ad_install.promotion>` するとすぐ昇格できる。

.. image:: ad_install/ad_install.10.png
    :scale: 50 %

ドメインコントローラに昇格
-----------------------------

Acitive　Drectory ドメイン構成ウィザードの起動
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

サーバーマネージャで AD DSを選択し、「その他」をクリック。

.. image:: ad_install/ad_install.11.png
    :scale: 50 %

「このサーバーをドメインコントローラに昇格」をクリック。

.. image:: ad_install/ad_install.12.png
    :scale: 50 %

.. _ad_install.promotion:

ドメインを構成しして昇格
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Active Directoryドメインサービス構成ウィザードが起動される。

.. image:: ad_install/ad_install.13.png
    :scale: 50 %


配置構成、の画面になるので、

.. image:: ad_install/ad_install.14.png
    :scale: 50 %

「新しいフォレストを追加する」をクリックし、「ルートドメイン名」を入力。ここでは openid.local

.. image:: ad_install/ad_install.15.png
    :scale: 50 %

ドメインコントローラオプション。ここでパスワード指定（わすれないこと！）

.. image:: ad_install/ad_install.16.png
    :scale: 50 %

DNSオプション。

`新しい Windows Server 2008 ドメイン コントローラーまたは Windows Server 2008 R2 ドメイン コントローラーを DNS サーバーと共に treyresearch5.net などのドメインにインストールする場合 <http://technet.microsoft.com/ja-jp/library/cc754463(v=ws.10).aspx>`_ ということで、要するにLANの環境であれば、


::

    他のドメイン内またはインターネット上のユーザーが、
    ローカル ドメイン内のコンピューター名の 
    DNS 名のクエリを解決しないことに問題がない場合は、
    メッセージを無視し、[はい] をクリックします。

ということです。

.. image:: ad_install/ad_install.17.png
    :scale: 50 %

OK

.. image:: ad_install/ad_install.18.png
    :scale: 50 %

NetBIOS ドメイン名はそのまま

.. image:: ad_install/ad_install.19.png
    :scale: 50 %

パス関係もそのまま

.. image:: ad_install/ad_install.20.png
    :scale: 50 %

オプションの確認

.. image:: ad_install/ad_install.21.png
    :scale: 50 %

これは、 ::

    新しいフォレストの最初の Active Directory ドメイン コントローラーとしてこのサーバーを構成します。

    新しいドメイン名は "openid.local" です。これは新しいフォレスト名にもなります。
    ドメインの NetBIOS 名: OPENID
    フォレストの機能レベル: Windows Server 2012 R2
    ドメインの機能レベル: Windows Server 2012 R2

    追加オプション:

        グローバル カタログ: はい
        DNS サーバー: はい
        DNS 委任の作成: いいえ

    データベース フォルダー: C:\Windows\NTDS
    ログ ファイル フォルダー: C:\Windows\NTDS
    SYSVOL フォルダー: C:\Windows\SYSVOL
    DNS サーバー サービスはこのコンピューターに構成されます。
    このコンピューターは、この DNS サーバーを優先 DNS サーバーとして使用するように構成されます。

    新しいドメイン Administrator アカウントのパスワードはこのコンピューターのローカル Administrator アカウントのパスワードと同じものに設定されます。

次へ

.. image:: ad_install/ad_install.22.png
    :scale: 50 %

前提条件のチェック

1)

    Windows Server 2012 R2 ドメイン コントローラーには、
    セキュリティ設定 "Windows NT 4.0 と互換性のある暗号化アルゴリズムを許可する" 
    の既定値が設定されています。
    これにより、セキュリティ チャネル セッションを確立するときに、
    セキュリティの弱い暗号化アルゴリズムの使用は許可されなくなります。

    この設定の詳細については、サポート技術情報 (KB) の記事 942564 
    (http://go.microsoft.com/fwlink/?LinkId=104751) を参照してください。


2)

    このコンピューターには、IP プロパティに静的 IP アドレスが割り当てられていない
    物理ネットワーク アダプターが、少なくとも 1 つあります。

    ネットワーク アダプターで IPv4 と IPv6 の両方が有効にされている場合、
    そのネットワーク アダプターの IPv4 および IPv6 プロパティの両方に、
    IPv4 と IPv6 の両方の静的 IP アドレスを割り当てる必要があります。

    ドメイン ネーム システム (DNS) 動作を信頼できるものにするために、
    このような静的 IP アドレスの割り当てを、
    すべての物理ネットワーク アダプターに対して行う必要があります。

3)

    権限のある親ゾーンが見つからないか、Windows DNS サーバーが実行されていないため、
    この DNS サーバーの委任を作成できません。

    既存の DNS インフラストラクチャと統合する場合は、
    ドメイン "openid.local" 外からの名前解決が確実に行われるように、
    親ゾーンでこの DNS サーバーへの委任を手動で作成する必要があります。

    それ以外の場合は、何もする必要はありません。


よって、インストールをクリックして開始

.. image:: ad_install/ad_install.23.png
    :scale: 50 %

自動的にリブート

.. image:: ad_install/ad_install.24.png
    :scale: 50 %

