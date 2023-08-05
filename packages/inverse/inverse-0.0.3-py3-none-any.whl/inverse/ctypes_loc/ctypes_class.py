# pylint: disable=missing-class-docstring
import ctypes
from ctypes import *

# import numpy as np
from pathlib import Path

import os

import numpy as np

CDLL = cdll


class CTypeConversion:
    """"""

    def __init__(self, name):
        self.name = name
        self.so_name = name + ".so"
        self.so_name_linux = name + "SHARED.so"

    def start(self):
        curr_dir = os.path.dirname(__file__)

        # path = Path(r"C:\Users\coldwater80\Desktop\PyCharmProjects\inversePackage\inverse\ctypes")  # os.getcwd()
        path = Path(curr_dir)  # os.getcwd()

        if os.name == "nt":
            self.clibrary = ctypes.CDLL(os.path.join(path, self.so_name))

        else:
            # CDLL = cdll.LoadLibrary("libc.so.6")
            self.clibrary = cdll.LoadLibrary(os.path.join(path, self.so_name_linux))

            # clibrary = ctypes.cdll(os.path.join(path, "clibrary.so"))

        # self.free_memory_func_float = self.clibrary.free_memory_float
        # self.free_memory_func_double = self.clibrary.free_memory_double
        self.multip()
        self.operate_inside()

    def multip(self):
        self.clibrary.multiplyVector_double.restype = ctypes.POINTER(ctypes.c_double)
        self.clibrary.multiplyVector_double.argtypes = [
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_int,
            ctypes.c_double,
        ]

    def operate_inside(self):
        self.clibrary.operate_inside_double.argtypes = [
            ctypes.c_double,
            ctypes.c_double,
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_int,
        ]

        self.clibrary.operate_inside_double.restype = ctypes.POINTER(ctypes.c_double)

    # def free_memory(self, mult) -> None:
    #     self.free_memory_func(mult)

    def test_get_result(self, num=10) -> list:
        return self.get_result(10, 2)

    def get_result(self, num, multiplier) -> list:
        values = (ctypes.c_float * num)()
        for i in range(num):
            values[i] = i

        result_pointer = self.clibrary.multiplyVector(values, len(values), multiplier)
        mylist = result_pointer[:num]
        self.clibrary.free_memory_float(result_pointer)
        return mylist

    def get_result_mult(self, array, multiplier) -> list:
        num = len(array)
        values = (ctypes.c_double * num)()
        for i in range(num):
            values[i] = array[i]

        result_pointer = self.clibrary.multiplyVector_double(values, num, multiplier)
        mylist = result_pointer[:num]
        self.clibrary.free_memory_double(result_pointer)

        return mylist

    def get_result_opt(self, num1, num2, array1, array2, size) -> list:
        values1 = (ctypes.c_double * size)()
        values2 = (ctypes.c_double * size)()
        for i in range(size):
            values1[i] = array1[i]
            values2[i] = array2[i]

        result_pointer = self.clibrary.operate_inside_double(
            num1, num2, values1, values2, size
        )
        mylist = result_pointer[:size]
        self.clibrary.free_memory_double(result_pointer)

        return mylist


deneme_vector = CTypeConversion("vector_ops")
deneme_vector.start()


def c_multiply(array, multiplier):
    return deneme_vector.get_result_mult(array, multiplier)


def c_divide(array, multiplier):
    return deneme_vector.get_result_mult(array, 1 / multiplier)


def py_operate_inside_double(num1, num2, array1, array2, size):
    return deneme_vector.get_result_opt(num1, num2, array1, array2, size)


def py_equivalent_operate_inside_double(num1, num2, array1, array2, size):
    factor = num1 / num2 if num2 != 0 else 0
    array1 = np.array(array1)  # 3 array
    array2 = np.array(array2)  # 4 array
    nrow = array1 - c_multiply(array2, factor)
    return nrow.tolist()

    # nrow = py_operate_inside_double(number_j, number_i, row_J, row_i, len(row_J))


py_operate_inside_double_quick = py_operate_inside_double
c_divide_quick = c_divide

if __name__ == "__main__":
    c_multiply([10, 20], 2)
    c_divide([10, 20], 2)

__all__ = [
    "c_multiply",
    "c_divide",
    "py_operate_inside_double",
    "py_operate_inside_double_quick",
]
