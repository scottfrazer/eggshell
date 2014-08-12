from setuptools import setup

version = '1.0'
long_description = 'Eggshell is a shell interface'

setup(
  name='eggshell',
  version=version,
  description=long_description,
  author='Scott Frazer',
  author_email='scott.d.frazer@gmail.com',
  packages=['eggshell'],
  package_dir={'eggshell': 'eggshell'},
  license = 'MIT',
  keywords = "Bash, Shell",
  url = "http://github.com/scottfrazer/eggshell",
  classifiers=[
      'License :: OSI Approved :: MIT License',
      "Programming Language :: Python",
      "Development Status :: 4 - Beta",
      "Intended Audience :: Developers",
      "Natural Language :: English"
  ]
)
