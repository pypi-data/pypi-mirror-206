
import ctypes
from ctypes import *
from pathlib import Path
import os
import platform
from functools import lru_cache 



@lru_cache(maxsize=128, typed=False)
def get_platform():
    if platform.system() == 'Darwin' and os.name == 'posix':
        return 'Mac'
    elif os.name == 'nt':
        return 'Windows'
    return 'Linux'


@lru_cache(maxsize=128, typed=False)
def get_c_file_for_platform(name_of_file='clib.c'):
    platform_name = get_platform()
    c1 = {
        'Windows': 'clibrary.so',
        'Linux': 'clibSHARED.so',
        'Mac': 'clibMAC'
    }
    c2 = {
        'Windows': 'vector_ops.so',
        'Linux': 'vector_opsSHARED.so',
        'Mac': 'vector_opsMAC'
    }
    cfiles = {
        'clib.c': c1,
        'vector_ops.c': c2
    }
    return cfiles[name_of_file][platform_name]


@lru_cache(maxsize=128, typed=False)
def get_c_lib(name_of_file='clib.c'):
    obj = {'Windows': ctypes.CDLL,
           'Linux': cdll.LoadLibrary,
           'Mac':  cdll.LoadLibrary}
    fnc = obj[get_platform()]
    file_name = get_c_file_for_platform(name_of_file)
    path = Path(os.path.dirname(__file__))
    file_name_full = os.path.join(path, file_name)

    return fnc(file_name_full)


__all__ = [
    'get_c_lib'
]
