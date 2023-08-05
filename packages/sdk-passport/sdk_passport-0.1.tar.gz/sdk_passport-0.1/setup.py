from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='sdk_passport',
  version='0.1',
  description='A library for capturing image',
  long_description=open('README.rst').read()+ '\n\n',
  long_description_content_type='text/x-rst',
  url='https://github.com/arijitdatta123/sdk_passport.git',
  author='Arijit Datta',
  author_email='dattarijit97@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='password',
  packages=find_packages(),
  install_requires=['']
)