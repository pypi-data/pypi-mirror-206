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
  version='0.0.8',
  description='''ASCE is a simple program that operates on matrices''',
  long_description='''ASCE is a simple program that operates on matrices. Some of the operations are:add, substract, multiply,triangle_inf, triangle_sup, determinant,trace,inverse... The purpose of this project is to find an algorithm that can multiply matrices with a better time complexity than the normal code(Strassen)''',
  url='',  
  author='CZB ASCE GROUP',
  author_email='sandrine.sila@net.usj.edu.lb',
  license='MIT', 
  classifiers=classifiers,
  keywords='library', 
  packages=find_packages()
)