<?php

//Authコンポーネントを使います
//http://book.cakephp.org/2.0/ja/core-utility-libraries/app.html 

App::uses('AuthComponent',          //パッケージ名
          'Controller/Component');  //クラス名


class UserTest              // 規約:このテストスクリプトはUserTest.phpにするこｔ 
    extends CakeTestCase    // 規約:必ずどれかを継承 
                            //(CakeTestCase, ControllerTestCase, PHPUnit_Framework_TestCase)
{
    public function testValidation() //規約:メソッド名は test****() 

                                   //(@testアノテーションも使える)
    {
        $this->User = ClassRegistry::init('User');

        $this->User->create(array(
            'username' => 'hogehoge',
            'password' => ''
         ));
    
        $results = $this->User->invalidFields();

        $this->assertEquals(array_key_exists('username', $results), false);
        $this->assertEquals(array_key_exists('password', $results), true);
    }

    public function testImport(){
        $this->User = ClassRegistry::init('User');
        $res = $this->User->import("somwhere");

        $this->assertEqual(count($res['messages']), 0);
        $this->assertEqual(count($res['errors']), 0);
    }
}
?>

