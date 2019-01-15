from bs4 import BeautifulSoup as Soup
import os 

SAMPLE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'AllGolfExample')

MANIFEST = os.path.join(
    SAMPLE, 'imsmanifest.xml')

def manifest(path=MANIFEST):
    return Soup(open(path)).select('manifest')[0]


m = manifest()
for t in m.select('organizations organization title'):
    print t
