from setuptools import setup, find_packages
classifiers = [
 'Development Status :: 5 - Production/Stable',
 'Intended Audience :: Education',
 'Operating System :: Microsoft :: Windows :: Windows 10',
 'License :: OSI Approved :: MIT License',
 'Programming Language :: Python :: 3'
]
setup(
  name='thiennguyen',
  version='0.0.1',
  description='Day la test thu vien tinh toan 2 so',
  long_description=open('README.txt').read() + '\n\n' +
open(' CHANGELOG.txt').read(),
  url='',
  author='thiennguyen',
  author_email='minhthien16111996@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='thiennguyen',
  packages=find_packages(),
  install_requires=['']
)