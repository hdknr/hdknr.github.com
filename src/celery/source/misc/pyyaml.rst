::

    (tact)hdknr@wzy:~/ve/tact/src/paloma/example/app$ pip install pyyaml
    
    Downloading/unpacking pyyaml
      Downloading PyYAML-3.10.tar.gz (241Kb): 241Kb downloaded
      Running setup.py egg_info for package pyyaml
    
    Installing collected packages: pyyaml
      Running setup.py install for pyyaml
        checking if libyaml is compilable
        gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c build/temp.linux-x86_64-2.7/check_libyaml.c -o build/temp.linux-x86_64-2.7/check_libyaml.o
        checking if libyaml is linkable
        gcc -pthread build/temp.linux-x86_64-2.7/check_libyaml.o -lyaml -o build/temp.linux-x86_64-2.7/check_libyaml
        building '_yaml' extension
        gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c ext/_yaml.c -o build/temp.linux-x86_64-2.7/ext/_yaml.o
        In file included from ext/_yaml.c:223:0:
        ext/_yaml.h:6:0: warning: "PyUnicode_FromString" redefined [enabled by default]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:281:0: note: this is the location of the previous definition
        ext/_yaml.c: In function ‘__pyx_pf_5_yaml_get_version_string’:
        ext/_yaml.c:1145:17: warning: assignment discards ‘const’ qualifier from pointer target type [enabled by default]
        ext/_yaml.c: In function ‘__pyx_pf_5_yaml_7CParser___init__’:
        ext/_yaml.c:2074:38: warning: passing argument 2 of ‘yaml_parser_set_input’ from incompatible pointer type [enabled by default]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:1367:1: note: expected ‘int (*)(void *, unsigned char *, size_t,  size_t *)’ but argument is of type ‘int (*)(void *, char *, int,  int *)’
        ext/_yaml.c:2272:45: warning: pointer targets in passing argument 2 of ‘yaml_parser_set_input_string’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:1341:1: note: expected ‘const unsigned char *’ but argument is of type ‘char *’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_7CParser__token_to_object’:
        ext/_yaml.c:3705:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:3705:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:3718:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:3718:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4285:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4285:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4339:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4339:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4393:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4393:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4406:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4406:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:4493:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_7CParser__event_to_object’:
        ext/_yaml.c:5909:9: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:5909:9: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:5922:9: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:5922:9: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6088:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6088:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6163:7: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6163:7: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6200:7: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6200:7: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6216:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6520:7: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6520:7: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6557:7: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6557:7: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6747:7: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6747:7: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6784:7: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:6784:7: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_7CParser__compose_node’:
        ext/_yaml.c:8064:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8064:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8284:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8284:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8315:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8315:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8346:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:8346:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_7CParser__compose_scalar_node’:
        ext/_yaml.c:8861:3: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:9019:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:9019:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_7CParser__compose_sequence_node’:
        ext/_yaml.c:9461:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:9461:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_7CParser__compose_mapping_node’:
        ext/_yaml.c:9998:5: warning: pointer targets in passing argument 1 of ‘strlen’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:38:0,
                         from ext/_yaml.c:4:
        /usr/include/string.h:399:15: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c:9998:5: warning: pointer targets in passing argument 1 of ‘PyUnicodeUCS4_DecodeUTF8’ differ in signedness [-Wpointer-sign]
        In file included from /usr/include/python2.7/Python.h:85:0,
                         from ext/_yaml.c:4:
        /usr/include/python2.7/unicodeobject.h:750:23: note: expected ‘const char *’ but argument is of type ‘yaml_char_t *’
        ext/_yaml.c: In function ‘__pyx_pf_5_yaml_8CEmitter___init__’:
        ext/_yaml.c:11065:38: warning: passing argument 2 of ‘yaml_emitter_set_output’ from incompatible pointer type [enabled by default]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:1829:1: note: expected ‘int (*)(void *, unsigned char *, size_t)’ but argument is of type ‘int (*)(void *, char *, int)’
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_8CEmitter__object_to_event’:
        ext/_yaml.c:12199:44: warning: pointer targets in assignment differ in signedness [-Wpointer-sign]
        ext/_yaml.c:12300:44: warning: pointer targets in assignment differ in signedness [-Wpointer-sign]
        ext/_yaml.c:12563:5: warning: pointer targets in passing argument 2 of ‘yaml_alias_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:553:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13168:5: warning: pointer targets in passing argument 2 of ‘yaml_scalar_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:578:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13168:5: warning: pointer targets in passing argument 3 of ‘yaml_scalar_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:578:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13168:5: warning: pointer targets in passing argument 4 of ‘yaml_scalar_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:578:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13521:5: warning: pointer targets in passing argument 2 of ‘yaml_sequence_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:601:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13521:5: warning: pointer targets in passing argument 3 of ‘yaml_sequence_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:601:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13874:5: warning: pointer targets in passing argument 2 of ‘yaml_mapping_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:633:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:13874:5: warning: pointer targets in passing argument 3 of ‘yaml_mapping_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:633:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c: In function ‘__pyx_pf_5_yaml_8CEmitter_6serialize’:
        ext/_yaml.c:15082:42: warning: pointer targets in assignment differ in signedness [-Wpointer-sign]
        ext/_yaml.c:15183:42: warning: pointer targets in assignment differ in signedness [-Wpointer-sign]
        ext/_yaml.c: In function ‘__pyx_f_5_yaml_8CEmitter__serialize_node’:
        ext/_yaml.c:15863:5: warning: pointer targets in passing argument 2 of ‘yaml_alias_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:553:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:16500:7: warning: pointer targets in passing argument 2 of ‘yaml_scalar_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:578:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:16500:7: warning: pointer targets in passing argument 3 of ‘yaml_scalar_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:578:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:16500:7: warning: pointer targets in passing argument 4 of ‘yaml_scalar_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:578:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:16790:7: warning: pointer targets in passing argument 2 of ‘yaml_sequence_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:601:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:16790:7: warning: pointer targets in passing argument 3 of ‘yaml_sequence_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:601:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:17193:7: warning: pointer targets in passing argument 2 of ‘yaml_mapping_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:633:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        ext/_yaml.c:17193:7: warning: pointer targets in passing argument 3 of ‘yaml_mapping_start_event_initialize’ differ in signedness [-Wpointer-sign]
        In file included from ext/_yaml.h:2:0,
                         from ext/_yaml.c:223:
        /usr/include/yaml.h:633:1: note: expected ‘yaml_char_t *’ but argument is of type ‘char *’
        gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-x86_64-2.7/ext/_yaml.o -lyaml -o build/lib.linux-x86_64-2.7/_yaml.so
    
    Successfully installed pyyaml
    Cleaning up...
