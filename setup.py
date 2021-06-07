#!/usr/bin/env python3
from setuptools import setup


setup(name='btre',
      version=1,
      install_requires=['clipboard'],
      description='A regex string tool',
      author='nacly',
      url='https://www.github.com/na-cly/btre',
      python_requires='>=3.6',
      scripts=['bin/btre'],
      packages=['btre'],
      license='MIT',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: text'
      ],
      keywords=('regex'))