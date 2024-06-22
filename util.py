# -*- coding: utf-8 -*-
import sys


def custom_reload(module):
    if get_python_major_version() == 2:
        reload(module)      # Python2系
    else:
        import importlib    # Python3系
        importlib.reload(module)


def get_python_major_version():
    ver = sys.version
    major_ver = ver.split('.')[0]
    return int(major_ver)
