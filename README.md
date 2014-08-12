Eggshell
========

A Simpler Python interface to the shell

Installation
============

    pip install eggshell

Usage
=====

    $ python
    Python 3.4.0 (default, May  8 2014, 15:33:16)
    [GCC 4.1.2 20080704 (Red Hat 4.1.2-48)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import eggshell
    >>> (rc, stdout, stderr) = eggshell.run('ls')
    >>> print(stdout)
    eggshell
    README.md
    setup.py
    >>>
