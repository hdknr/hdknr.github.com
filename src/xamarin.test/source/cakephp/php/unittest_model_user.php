<?php

App::uses('AppModel', 'Model');

// SimplePasswordHasher
// - http://api.cakephp.org/2.4/class-SimplePasswordHasher.html
App::uses('SimplePasswordHasher', 
          'Controller/Component/Auth');


class User              // app/Model/User.php に保存します
    extends AppModel
{

    var $name='User';

    public $validate = array(
        'username' => array(
            'required' => array(
                'rule' => array('notEmpty'),
                'message' => 'A username is required'
            )
        ),
        'password' => array(
            'required' => array(
                'rule' => array('notEmpty'),
                'message' => 'A password is required'
            )
        ),
        'role' => array(
            'valid' => array(
                'rule' => array('inList', array('admin', 'author')),
                'message' => 'Please enter a valid role',
                'allowEmpty' => false
            )
        )
    );
    var $belongsTo = array();

    // alias : https://stackoverflow.com/questions/4275154/what-is-cakephp-model-alias-used-for
    // - $this->alias is the name of the model.
    // - If your model is User, then you must do that on $data to get the correct value.
    // - $data['User']['password'] is equivalent to: 
    //   $data[$this->alias][$password_field] 

    public function beforeSave($options = array()) {
        if (isset($this->data[$this->alias]['password'])) {
            $passwordHasher = new SimplePasswordHasher();
            $this->data[$this->alias]['password'] = $passwordHasher->hash($this->data[$this->alias]['password']);
        }
        return true;
    }

    function import($filename)
    {    
        $return = array(
            'messages' => array(),
            'errors' => array(),
        );
       
        return $return;
    }
}

