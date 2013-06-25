======================
Start URLConf
======================

.. contents:: Start URLConf
    :local:

reverseの遅延評価を使う
========================================

- settings.pyなどurls.pyが評価されていない場所で :ref:`django.core.urlresolvers.reverse` を使うとエラーが起きる場合がある
- そういう場合は、 :ref:`django.core.urlresolvers.reverse_lazy` で遅延評価させる

