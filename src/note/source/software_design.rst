=====================
Software Design
=====================

.. contents::
    :local:

Modeling
==================

.. glossary::

    PDS
    Presentation Domain Separation
        - アプリケーションをPresentationとそれ以外の部分に分割しようとする基本的な考え方       
        - :term:`MVC` は PDS を実現する１手段
        - http://martinfowler.com/bliki/PresentationDomainSeparation.html 
        - http://capsctrl.que.jp/kdmsnr/wiki/bliki/?PresentationDomainSeparation

    MVC
    Model View Controller
        - http://ja.wikipedia.org/wiki/Model_View_Controller 
        

    MVVM
    Model View ViewModel
        - 実質 :term:`Presentation Model` ?
        - http://ja.wikipedia.org/wiki/Model_View_ViewModel
        - http://ugaya40.net/architecture/mvvm_to_mvc.html

    Presentation Model
        - http://martinfowler.com/eaaDev/PresentationModel.html


GoF
======

Flyweight
----------

- 「フライ級」 ( ヘビー、ミドル、ライト 、フライ )
- 同じインスタンスを共有することで、無駄なインスタンスを生成しないようにして、 プログラム全体を軽くすることを目的としたパターン
- 共有できるものは共有するという考え方により、 メモリの消費量を節約
- http://ja.wikipedia.org/wiki/Flyweight_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
