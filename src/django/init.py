import os

top='/home/hdknr/ve/main/lib/python2.6/site-packages/django'
dst="tmp/%s.rst"
cheat="tmp/cheat/%s.rst"
index="tmp/files.rst"
svn='https://code.djangoproject.com/browser/django/trunk/django'

index_file = open(index,"w")
for root, dirs, files in os.walk(top, topdown=True):
    if os.path.isfile(root+'/__init__.py') == False:
        continue
    rstname = "django" + root.replace(top,'').replace('/','.')

    index_file.write("    %s\n" % rstname )

    rstfile = open( dst % rstname , "w")
    rstfile.write( "=" * len(rstname) + "\n")
    rstfile.write( rstname   + "\n")
    rstfile.write( "=" * len(rstname)+ "\n\n" )
    
    rstfile.write(".. contents:: %s\n\n" % rstname )

    cheat_file = open(cheat % rstname, "a")
    cheat_file.write('')
    cheat_file.close()

    rstfile.write( ".. _%s:" % rstname + "\n")
    rstfile.write("\n"  )
    rstfile.write( rstname +"\n")
    rstfile.write( "="* len(rstname )+"\n" )

    rstfile.write( "\n\n- `source <%s%s/__init__.py>`_ \n" % (svn,root.replace(top,'')) ) 

    rstfile.write( "\n.. include:: cheat/%s.rst" % rstname +"\n\n")

    rstfile.write("" +"\n" )
    rstfile.write( ".. automodule:: %s" % rstname+"\n" )
    rstfile.write( "    :members:"+"\n" )
    rstfile.write(""  +"\n")
    rstfile.write("" +"\n" )

    if len(dirs) > 1:
        rstfile.write( "Sub" +"\n")
        rstfile.write( "====" +"\n")
        rstfile.write( "" +"\n")
        dirs.sort()
        for name in dirs:
            if os.path.isfile(root+'/%s/__init__.py' % name ) == False:
                continue
            rstfile.write( "- :doc:`%s.%s`" % (rstname,name ) +"\n")
            rstfile.write("\n"  )

    files.sort() 
    for name in files:
        base,ext = os.path.splitext(name)
        if ext != '.py' or base == '__init__' : 
            continue
        modname = "%s.%s" % (rstname,base) 

        cheat_file = open(cheat % modname, "a")
        cheat_file.write('')
        cheat_file.close()
 
        rstfile.write( ".. _%s:" % modname +"\n")
        rstfile.write(""  +"\n")
        rstfile.write( modname+"\n" )
        rstfile.write( '=' * len(modname ) +"\n")

        rstfile.write( "\n\n- `source <%s%s/%s>`_ \n" % (svn,root.replace(top,''),name) ) 

        rstfile.write( "\n.. include:: cheat/%s.rst" % modname +"\n\n")
        
        rstfile.write( ".. automodule:: %s" % modname +"\n")
        rstfile.write( "    :members:" +"\n")
        rstfile.write(""  +"\n")

    rstfile.close()

index_file.close()
