=============
jQuery
=============

.. contents::
    :local:

ページロードされたときに処理する
===================================

.. code-block:: javascript

    $(document).ready(function(){
        alert("hello");
    });

親子関係
====================

孫を含んだ全ての子供
---------------------------

- children("decestors \*") のようにセレクタにアスタリスクを入れる


複数の除外
===========

- not(条件1,条件2,...)

.. code-block:: javascript

    // 現在の要素(多分<form/>) の子要素の中で
    // radioとcheckbox以外の<input/>と <textarea/>,<select/> 
    // だったら１つの値をとる

    $(this).find("input:not([type='radio'],[type='checkbox']),textarea,select")
    .each(function(){
        ret[$(this).attr('name')] =  $(this).val();
    });


フォーム送信の結果で部分画面を入れ替える
=============================================

.. code-block:: javascript

    function blockpost(form,container)
    {
        $.ajaxSettings.traditional = true; // For Django, not for PHP
        $.post( 
            $(form).attr('action'),
            $(form).serialize(),
            function(data) { 
                $(form).parents(container).html(data);
            }   
        );         
    }

- ファイルアップロードはこのやり方では出来ません
- Django テンプレート例

.. code-block:: html

    <div class="block"  />

    <h2>設問</h2>
    <div>
      <form id="vote-form" 
            action="{% url app_votes_block id=qid command='default' %}"  
            method="post"> {% csrf_token  %}  
        {{ form }}
        <input type="submit" name="submit" value="送信" />            
      </form>
    </div> 

    <script>
    $(function(){
        $("span.submit").click(function(){
            blockpost("#vote-form","div.block" );
        });
    });
    </script> 
    
    </div>

ファイルアップロード
==============================

- https://github.com/blueimp/jQuery-File-Upload 


UI
=====

- https://github.com/twitter/bootstrap
- http://jqueryui.com/
- https://github.com/addyosmani/jquery-ui-bootstrap
- http://masonry.desandro.com/
