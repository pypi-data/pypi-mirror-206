import sys, os
from setuptools import setup


TOP_LEVEL     = 'access2thematrix'
sys.path[0:0] = [os.path.join(os.getcwd(), TOP_LEVEL)]
pkg_info      = __import__('pkg_info')

#-------------------------------------------------------------------------------

DESCRIPTION      = 'Scienta Omicron (NanoScience) (NanoTechnology) MATRIX ' \
                   'Control System result file accessing tool'
LONG_DESCRIPTION = open('README.txt', 'rb').read().decode()
AUTHOR           = 'Stephan Zevenhuizen'
AUTHOR_EMAIL     = 'S.J.M.Zevenhuizen@uu.nl'
LICENSE          = 'BSD License'
CLASSIFIERS      = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Scientific/Engineering :: Chemistry
Topic :: Scientific/Engineering :: Information Analysis
Topic :: Scientific/Engineering :: Physics
Topic :: Software Development :: Libraries :: Python Modules
"""
KEYWORDS         = 'SPM scanning probe microscopy image analysis'
INSTALL_REQUIRES = ['numpy', 'six']
PYTHON_REQUIRES  = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4'
PACKAGES         = [TOP_LEVEL]

#-------------------------------------------------------------------------------

setup(name             = pkg_info.NAME,
      version          = pkg_info.VERSION,
      description      = DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      author           = AUTHOR,
      author_email     = AUTHOR_EMAIL,
      license          = LICENSE,
      classifiers      = [c for c in CLASSIFIERS.split('\n') if c],
      keywords         = KEYWORDS,
      install_requires = INSTALL_REQUIRES,
      python_requires  = PYTHON_REQUIRES,
      zip_safe         = False,
      packages         = PACKAGES)
