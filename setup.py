from setuptools import setup

version = '1.0'
long_description = 'Conch is a shell interface'

setup(
  name='conch',
  version=version,
  description=long_description,
  author='Scott Frazer',
  author_email='scott.d.frazer@gmail.com',
  packages=['conch'],
  package_dir={'conch': 'conch'},
  license = 'MIT',
  keywords = "Bash, Shell",
  url = "http://github.com/scottfrazer/conch",
  classifiers=[
      'License :: OSI Approved :: MIT License',
      "Programming Language :: Python",
      "Development Status :: 4 - Beta",
      "Intended Audience :: Developers",
      "Natural Language :: English"
  ]
)
