docs={}
docs["oauth_res_reg.rst"]= [
    "abstract.rst",
    "1.rst",
    "1.1.rst",
    "1.2.rst",
    "1.3.rst",
    "2.rst",
    "2.1.rst",
    "2.2.rst",
    "2.3.rst",
    "2.3.1.rst",
    "2.3.2.rst",
    "2.3.3.rst",
    "2.3.4.rst",
    "2.3.5.rst",
    "3.rst",
    "4.rst",
    "5.rst",
    "6.rst",
    "7.rst",
    "8.rst",
    "11.rst",
    "11.1.rst",
    "11.2.rst",
]
import os
fname='oauth_res_reg.rst'

dname,dext= os.path.splitext(fname)

for i in docs[fname]:
    name,ext = os.path.splitext(i)
    print ".. _%s.%s:\n" % (dname,name)
    print ".. include:: %s/%s\n" % (dname,i)
    

