from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='NaClPy',
  version='0.02a',
  description='Minimal Client-Server-Communication Libraty',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='Johanna Heidel',
  author_email='hdljohanna@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['nacl','network','networking'], 
  packages=find_packages(),
  install_requires=['flask','cryptography','requests'] 
)
