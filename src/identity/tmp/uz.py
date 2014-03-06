from zipfile import ZipFile
import os
import sys
from StringIO import StringIO


def unzip(src,outdir='.'):
    _unzip = lambda z,out : map(lambda n:  z.extract(n, out),
                                z.namelist())

    if not os.path.exists(outdir):
        os.makedirs(outdir)
    
    if not sys.stdin.isatty() :
        _unzip(ZipFile(StringIO(sys.stdin.read())), outdir)
    
    elif src:
        with stream or open(src) as stream:
            _unzip(ZipFile(StringIO(sys.stdin.read())), outdir)
    

def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Unzip stdin or specifile file.')
    parser.add_argument('zipfile', metavar='ZIPFILE', type=str, nargs='?',
                   help='File to be unziped.')

    parser.add_argument('--dst', dest='destination',
                        default='_unzip', required=False, )

    parser.add_argument('--setup', dest='setup', action='store_true',
                        required=False, )


    args = parser.parse_args()

    if args.setup:
        sys.argv = [__file__,'install']
        setup_me() 
    else:
        unzip(args.zipfile, args.destination)

def setup_me():
    from setuptools import setup

    setup(
        name = 'uz.py',
        version = "1",
        license = 'Simplfied BSD License',
        author = 'Hideki Nara of LaFoaglia,Inc.',
        author_email = 'gmail [at] hdknr.com',
        maintainer = 'LaFoglia,Inc.',
        maintainer_email = 'gmail [at] hdknr.com',
        url = 'https://github.com/hdknr/uz',
        description = "uz : Unzip",
        long_description = "unzip script",
        download_url = 'https://github.com/hdknr/uz',
        platforms=['any'],
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Library',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Simplifed BSD License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
        ],
        scripts= [os.path.abspath(__file__)]
    )

if __name__ == '__main__':
    main()
