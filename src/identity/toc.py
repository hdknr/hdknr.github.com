import os
import glob
import re

def section_cmp(x,y ):
    X=x.split('.') 
    Y=y.split('.')

    #:abstract always WIN
    if X[0] == 'head':
        return -1 
    if Y[0] == 'head':
        return 1

    #:abstract always WIN
    if X[0] == 'abstract':
        return -1 
    if Y[0] == 'abstract':
        return 1

    LEN= min(len(X),len(Y))
    for i in range(0,LEN):
        if re.search(r"^\d+$",X[i]+Y[i]):
            ret = cmp(int(X[i]),int(Y[i] ) )
        else:
            ret = cmp(X[i],Y[i])

        if ret != 0:
            return ret

    return cmp( len(X),len(Y) )
      
SECTION=lambda pathname: os.path.splitext(os.path.basename(pathname))[0]

def get_sections(spec):
    sections = [ SECTION(i)   for i in glob.glob("source/%s/*.rst" % spec ) ]
    sections.sort(cmp=section_cmp )
    return sections

def make(spec,command='make') :
        
    sections = get_sections(spec)
    if command== 'sections':
        for section in sections:
            L=len(section.split('.'))
            print "  " * (L-1),section
        return
    
    FMT='''
.. _%(DOC)s.%(SECTION)s:
    
.. include:: %(DOC)s/%(SECTION)s.rst
'''
    
    for section in sections: 
        print FMT % { "DOC":spec, "SECTION": section }
        print

if __name__ == '__main__':
    import sys  
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('spec',metavar='SpecName',)
    parser.add_argument('command',metavar='Command',nargs='?',default='make',)
    args = parser.parse_args()

    make(args.spec,args.command)
