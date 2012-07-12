===========================
Python / C#
===========================

.. list-table::
    :widths: 20 40 40

    *   - 
        - Python
        - C# 

    *   - in 
        - in operator

            .. code-block:: python
    
                x = ['a','b','c']
                if 'a' in x:
                    print "Yes"

        - `Collection\<T\>.Contains <http://msdn.microsoft.com/en-us/library/ms132407.aspx>`_

            .. code-block:: csharp

                string[] animal = new string[] { "Whale","Leopard", "Panda" };
                if (animal.Contains<string>("Whale"))
                {
                    Console.WriteLine("Yes");
                }
