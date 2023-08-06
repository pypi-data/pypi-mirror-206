from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='ASCE',
  version='0.0.5',
#   description='A fast library/similar to numpy',
#   long_description=open('README.txt').read()
  url='',  
  author='CZB ASCE GROUP',
  author_email='sandrine.sila@net.usj.edu.lb',
  license='MIT', 
  classifiers=classifiers,
  keywords='library', 
  packages=find_packages(),
  install_requires=['math'] 
)