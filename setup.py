from setuptools import setup, find_packages

setup(
  name = 'jsonp2json',
  version = '1.0',
  packages = find_packages(),
  license = "MIT",
  description = 'Converts JSONP response to JSON format',
  author = 'Yong Cheng Toh',
  author_email = 'tohyongcheng@gmail.com',
  url = 'https://github.com/tohyongcheng/jsonp2json', 
  keywords = ['json', 'jsonp', 'parse', 'convert'], # arbitrary keywords
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3'
  ],
)