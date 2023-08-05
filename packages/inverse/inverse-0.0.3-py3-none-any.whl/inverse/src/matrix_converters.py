from typing import Protocol

from rich.progress import Progress

from inverse.ctypes_loc.ctypes_class import c_divide, c_multiply, py_operate_inside_double
from .abstract_data import id_ekle
from .abstract_data2 import DBDataOpt
from .buffer_ops import Buffer
from .check_result import inverse_check
from .measure_calls import CallStack
from .tuple_for_buffer import get_tuple_for_buffer
from .sp_matrix_ops import combine_row_op, divide_pivot, display_matrix_ozet, divide_pivot_eski, combine_row_op_eski

import numpy as np


class MatrixCreator(Protocol):
    ...


class BigMatrix:
    def __init__(self, name: str, n: int, threshold: int):
        self.name = name
        self.n = n
        self.db_rep = DBDataOpt(threshold=threshold, name=self.name)
        self.threshold = threshold
        # post init
        self.buffer = Buffer(self)

    def get_current_matrix(self):
        return self.buffer.get_current_matrix()

    def display(self):
        print("I am a big matrix")

    def check(self):
        print("I am a big matrix")

    def inverse(self):
        print("I am a big matrix")
        inverse_mat = self.sp_inverse()
        return self

    def save_on_begin_rand(self, matrix: np.array):

        self.db_rep.save_on_begin_rand(matrix)

    def save_on_begin_bigmatrix_lines(self, lines):

        self.db_rep.save_on_begin_bigmatrix_lines(lines)

    def sp_inverse(self) -> np.array:
        """TODO"""
        global CallStack
        from inverse import tic, toc

        tic()
        bucket = get_tuple_for_buffer(self.n, self.threshold)
        for sira in bucket:
            CallStack["dıs_dongu"] += 1
            sira = tuple(int(x) for x in sira if x < self.n and x > -1)
            i, *y = sira
            y = tuple(set(y))

            self.buffer.load_column_names_with_set(sira)
            # for i in [x]:
            row = tuple(self.buffer.get_row(i))
            pivot = row[i]

            row = c_divide(row, pivot)

            # SET Calculation
            self.buffer.set_row(i, row)

            for j in (a for a in y if a != i):
                CallStack["ic_dongu"] += 1
                number_j = self.buffer.get_cell(j, i)  # 1 number
                number_i = self.buffer.get_cell(i, i)  # 2 number

                # factor = number_j / number_i if number_i != 0 else 0
                row_J = np.array(self.buffer.get_row(j))  # 3 array
                row_i = np.array(self.buffer.get_row(i))  # 4 array
                # nrow = row_J - c_multiply(row_i, factor)

                nrow = py_operate_inside_double(number_j, number_i, row_J, row_i, len(row_J))

                # SET Calculation

                self.buffer.set_row(j, nrow)

        self.buffer.final_save()
        toc()
        inv_matrix = self.buffer.get_current_matrix()
        self.id_and_inv = inv_matrix
        # print(inv_matrix)

        return inv_matrix[:, self.n:]

    def sp_inverse_progress(self) -> np.array:
        """TODO"""
        global CallStack

        with Progress() as progress:
            bucket = get_tuple_for_buffer(self.n, self.threshold)
            task1 = progress.add_task("[red]Calculating...", total=len(bucket))
            for sira in bucket:
                CallStack["dıs_dongu"] += 1
                progress.update(task1, advance=1)
                # sira = tuple(x for x in sira if x < self.n)
                sira = tuple(int(x) for x in sira if x < self.n and x > -1)
                x, *y = sira
                y = tuple(set(y))

                self.buffer.load_column_names_with_set(sira)
                print("now x ", x, sira)
                for i in [x]:

                    row = tuple(self.buffer.get_row(i))
                    pivot = row[i]

                    print("Sıradaki satır numarası : ", i, "pivot :  ", pivot, "row", row, "*" * 10)
                    # exit()
                    row = divide_pivot(row, pivot)
                    self.buffer.set_row(i, row)
                    for j in y:
                        if i != j:

                            CallStack["ic_dongu"] += 1

                            number_j = self.buffer.get_cell(j, i)
                            number_i = self.buffer.get_cell(i, i)
                            if number_i != 0:
                                factor = number_j / number_i
                            else:
                                factor = 0
                            row_J = self.buffer.get_row(j)
                            row_i = self.buffer.get_row(i)
                            nrow = combine_row_op(row_J, row_i, factor)
                            self.buffer.set_row(j, nrow)
                            # print("setting nrow " , nrow )
        self.buffer.final_save()
        inv_matrix = self.buffer.get_current_matrix()
        self.id_and_inv = inv_matrix
        # print(inv_matrix)
        # return inv_matrix[:, self.n:]
        return inv_matrix


class BigMatrixConverter:
    def __init__(self, name):
        self.name = name

    def convert_small_to_bigmatrix(self,
                                   matrix: np.array,
                                   threshold: int) -> BigMatrix:
        big_matrix = BigMatrix(self.name, len(matrix), threshold)
        big_matrix.db_rep.save_on_begin_rand(matrix)
        return big_matrix

    def create_bigmatrix_from_lines(self, lines, name="test", threshold: int = 5) -> BigMatrix:
        ...
        big_matrix = BigMatrix(self.name, len(lines), threshold)
        big_matrix.db_rep.save_on_begin_rand(lines)
        return big_matrix


def test_small_matrix():
    from inverse import tic, toc, close_identity
    threshold = 500
    matrix = np.array([[19, 2, 3],
                       [8, 3, 6],
                       [7, 8, 15]])
    big_matrix = BigMatrixConverter("test").convert_small_to_bigmatrix(matrix, threshold)
    inverse_mat = big_matrix.sp_inverse()
    # inverse_mat2 = big_matrix.sp_inverse_progress()
    matrix_check = inverse_check(matrix)

    print(matrix, "matrix")
    print(inverse_mat, "inverse_mat")
    # print(inverse_mat2, "inverse_mat2")
    print(matrix_check, "matrix_check")

    sonuc1 = np.matmul(matrix, inverse_mat)
    # sonuc2 = np.matmul(matrix, inverse_mat2)
    sonuc3 = np.matmul(matrix, matrix_check)

    eps = 0.0001
    kontrol = close_identity(matrix=sonuc1, eps=eps)
    # kontrol2 = close_identity(matrix=sonuc2, eps=eps)
    kontrol2 = close_identity(matrix=sonuc3, eps=eps)
    print(CallStack)
