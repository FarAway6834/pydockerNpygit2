#!/usr/bin/python3 python
# -*- coding: utf-8 -*-
from subprocess import run as _r
from atexit import register as _e

_pip_uninstalling_text = 'pip uninstall'

_pip_uninstalling_argv = _pip_uninstalling_text.split()

_pip_uninstall = lambda : (lambda x : lambda v : (lambda work=x.append(v) : _r(x))())(copy(_pip_uninstalling))

_rm_self = lambda : _pip_uninstall('pydockerNpygit2')

def main():
    _e(_rm_self)
    _pip_uninstall('pygit2')
    _pip_uninstall('docker')

if __name__ == "__main__": main()
