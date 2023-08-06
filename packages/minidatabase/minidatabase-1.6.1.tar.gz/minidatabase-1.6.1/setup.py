from distutils.core import setup
from setuptools import find_packages
with open("README.rst", "r",encoding='gb18030',errors='ignore') as f:
  long_description = f.read()
setup(name='minidatabase',  
      version='1.6.1',  
      description='A tiny database system based on  python dictionary.',
      long_description=long_description,
      author='HansenL',
      author_email='hansenl@foxmail.com',
      url='http://osdn.xyz',
      install_requires=["requests","flask"],
      license=' GNU GENERAL PUBLIC LICENSE',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      entry_points={
"console_scripts":["minidb=minidatabase.minidb:main","webmdb=minidatabase.WebMDB:service"]
          }
      )
