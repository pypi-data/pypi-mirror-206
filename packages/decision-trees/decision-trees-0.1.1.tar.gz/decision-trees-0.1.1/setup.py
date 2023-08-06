from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='decision-trees',
  version='0.1.1',
  description='Decision Trees',
  long_description=open('README.md').read(),
  url='https://github.com/dananac/decision-tree',
  author='Dana Conley',
  author_email='dananaconley@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='password',
  packages=find_packages(),
  install_requires=[''],
)
