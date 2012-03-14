from docutils.parsers import rst
from docutils.utils import *

def main(name,filename):
    
    p = rst.Parser()
    doc = new_document( name )
    doc.settings.tab_width=4
    doc.settings.pep_references =1
    doc.settings.rfc_references =1
    p.parse( open(filename).read(),doc )


if __name__ == '__main__':
    main('dicsovery','source/common/table.discovery.provider.configuration.response.rst')
