====================
コントローラ
====================


.. contents::
    :local:


viewVars
==========

- Djangoで言うところのコンテキストdict

.. code-block:: php

    #AppConroller.php
    $this->set('userinfo',$userinfo);
    
    #PostController.php
    $this->viewVars['userinfo']


compact
---------

 - http://www.php.net/manual/ja/function.compact.php
 - http://www.php.net/manual/ja/function.extract.php


.. code-block:: php

    public function index(){
         
        $bar    = 'これはbarです。';
        $foo    = 'これはfooです。';
        $foobar = 'これはfoobarです。';
         
        $this->set(compact('bar', 'foo', 'foobar'));       
    }

Cake/Controller/Controller.php:

.. code-block:: php

    public function set($one, $two = null) {
        if (is_array($one)) {       // 配列だったら
            if (is_array($two)) {   // 二つ目も配列だったら
                $data = array_combine($one, $two);  //合体
            } else {
                $data = $one;
            }    
        } else {                    // 配列じゃなかったら
            $data = array($one => $two);    // key-valueのdict
        }    
        //  viewVarsを連結
        $this->viewVars = $data + $this->viewVars;
    }    

モデル
=======

モデル参照
------------

デフォルトモデル
^^^^^^^^^^^^^^^^^^^^^

- モデル名がコントローラ名と対応する名前を持つ場合、 CakePHP はそのモデルを自動的に呼び出し可能にします

.. code-block:: php

    class IngredientsController extends AppController {
        public function index() {
            //全ての ingredients を取得してビューに渡す
            $ingredients = $this->Ingredient->find('all');
            $this->set('ingredients', $ingredients);
        }
    }

    class Ingredient extends AppModel {
        public $name = 'Ingredient';
    }


paginate()
-------------
    
パジネータを用意する

.. code-block:: php
    
    public $paginate = array (
            'limit' => 10,
            'order' => array('created_at' => 'desc'),
    );

クエリを実行する

.. code-block:: php

    function index() { 
        // クエリのパラメータ
        $this->query = array('id' => 3 );

        // 実行
        $results = $this->paginate($this->query);
        //....
    }
