::

    (tact)hdknr@wzy:~/ve/tact/src/paloma/docs$ pip install pygraphviz

    Downloading/unpacking pygraphviz
      Downloading pygraphviz-1.1.zip (102Kb): 102Kb downloaded
      Running setup.py egg_info for package pygraphviz
        Trying pkg-config
        library_path=
        include_path=/usr/include/graphviz
        
        warning: no previously-included files matching '*~' found anywhere in distribution
        warning: no previously-included files matching '*.pyc' found anywhere in distribution
        warning: no previously-included files matching '.svn' found anywhere in distribution
        no previously-included directories found matching 'doc/build'
    Installing collected packages: pygraphviz
      Running setup.py install for pygraphviz
        Trying pkg-config
        library_path=
        include_path=/usr/include/graphviz
        building 'pygraphviz._graphviz' extension
        gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/graphviz -I/usr/include/python2.7 -c pygraphviz/graphviz_wrap.c -o build/temp.linux-x86_64-2.7/pygraphviz/graphviz_wrap.o
        pygraphviz/graphviz_wrap.c: In function ‘agattr_label’:
        pygraphviz/graphviz_wrap.c:2855:5: warning: return makes integer from pointer without a cast [enabled by default]
        gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-x86_64-2.7/pygraphviz/graphviz_wrap.o -lcgraph -lcdt -o build/lib.linux-x86_64-2.7/pygraphviz/_graphviz.so
        
        warning: no previously-included files matching '*~' found anywhere in distribution
        warning: no previously-included files matching '*.pyc' found anywhere in distribution
        warning: no previously-included files matching '.svn' found anywhere in distribution
        no previously-included directories found matching 'doc/build'
    Successfully installed pygraphviz
    Cleaning up...
    
