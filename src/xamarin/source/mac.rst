========================
Mac OSX
========================

.. contents::
    :local:

ダイアログボックス
=====================

- UIAlertView

    - https://developer.apple.com/library/ios/documentation/uikit/reference/UIAlertView_Class/UIAlertView/UIAlertView.html


.. code-block:: csharp

            new NSAlert {
                MessageText = "おはようございます",
                InformativeText = "よいお目覚めでしょうか?"
            }.RunSheetModal (this.Window);

iOS
----

.. code-block:: cshrap

            (new UIAlertView (
                url.ToString(),
                url.Path,  null, 
                "Cancel", "OK", "Perhaps")).Show();
