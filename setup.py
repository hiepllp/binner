import os, os.path
#from glob import iglob
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

from distutils.command.build_py import build_py
from distutils.command.install import install

class installsetup(install):
    def run(self):
        os.system("pip install -r requirements.txt")
	fpath = '/usr/bin/'
	ffpath = '/usr/'
        binnerpath=os.getcwd() + '/binner/'
	path = os.getcwd()
	bin_path = path + '/bin/'
	os.chdir(fpath)
	remove=['/usr/bin/binner-cli', '/usr/bin/binner-web']
	for i in remove:
	   if os.path.islink( i ):
	        os.remove( i )
        os.system('ln -s ' + path + '/bin/binner-cli /usr/bin/binner-cli')
        os.system('ln -s ' + path + '/bin/binner-web  /usr/bin/binner-web')
	os.chdir(path)
	install.run( self )


def finalizesetup():
	pass
 

setup(name="Binner",
      version="0.2.0",
      description="Calculate bin sizes for items. Easy!",
      maintainer="Nadir Hamid",
      maintainer_email="matrix.nad@gmail.com",
      url="https://",
      download_url = "https://pypi.python.org/pypi/",
      license="MIT",
      long_description="",
      packages=["binner"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Communications',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      cmdclass=dict(install=installsetup))
