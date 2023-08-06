from typing import Protocol

import numpy as np
from scipy.sparse import csc_matrix

from inverse.ctypes_loc.ctypes_class import c_divide, py_operate_inside_double_opt
from inverse.src.classes.abstract_data2 import DBDataOpt
from inverse.src.classes.buffer_ops import Buffer
from inverse.src.engine.algos.base_algo import basic_algo, basic_algo_sparse
from inverse.src.engine.base_classes.big_matrix_base import BigMatrixAbstract
from inverse.src.utils.check_result import inverse_check
from inverse.src.utils.tuple_for_buffer import get_tuple_for_buffer
from .algos._mappings import basic_algo_mappings
from .algos._spsparse import basic_algo_spsparse
from ..classes.sp_matrix import SPMatrix


class MatrixCreator(Protocol):
    ...


class BigMatrix(BigMatrixAbstract):
    def __init__(self, name: str, n: int, threshold: int):
        self.name = name
        self.n = n
        self.db_rep = DBDataOpt(threshold=threshold, name=self.name)
        self.threshold = threshold
        # post init
        self.buffer = Buffer(self)
        self.test = False

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

    def sp_inverse_hatali(self) -> np.array:
        """TODO"""
        global CallStack
        from inverse import tic, toc

        tic()
        bucket = get_tuple_for_buffer(self.n, self.threshold)

        for index, sira in enumerate(bucket):

            sira = tuple(int(x) for x in sira if x < self.n and x > -1)
            i, *y = sira
            y = tuple(set(y))
            sira_set = tuple(set(sira))
            self.buffer.load_column_names_with_set(sira_set)

            row = tuple(self.buffer.get_row(i))
            # pivot = row[i]

            # SET Calculation
            self.buffer.set_row(i, c_divide(row, row[i]))

            for j in (a for a in y if a != i):
                # CallStack["ic_dongu"] += 1
                # number_j = self.buffer.get_cell(j, i)  # 1 number
                # number_i = self.buffer.get_cell(i, i)  # 2 number

                # factor = number_j / number_i if number_i != 0 else 0
                row_J = tuple(self.buffer.get_row(j))  # 3 array
                row_i = tuple(self.buffer.get_row(i))  # 4 array
                # nrow = row_J - c_multiply(row_i, factor)

                nrow = py_operate_inside_double_opt(
                    i, row_J, row_i, len(row_J))
                # nrow = py_equivalent_operate_inside_double(i  , row_J, row_i, len(row_J))

                # SET Calculation

                self.buffer.set_row(j, nrow)

        self.buffer.final_save()
        toc()
        inv_matrix = self.buffer.get_current_matrix()
        self.id_and_inv = inv_matrix
        # print(inv_matrix)

        return inv_matrix[:, self.n:]

    def sp_inverse_with_spsparse(self, sp_matrix: SPMatrix) -> np.array:
        return basic_algo_spsparse(self, sp_matrix)

    def sp_inverse_with_mappings(self, mappings) -> np.array:

        return basic_algo_mappings(self, mappings)

    def sp_inverse(self) -> np.array:
        return basic_algo(self)

    def sp_sparse_inverse(self) -> np.array:
        return basic_algo_sparse(self)

    def sp_inverse_progress(self) -> np.array:
        return basic_algo_mappings(self)


class BigMatrixConverter:
    def __init__(self, name):
        self.name = name

    def convert_small_to_bigmatrix(self,
                                   matrix: np.array,
                                   threshold: int) -> BigMatrix:
        big_matrix = BigMatrix(self.name, len(matrix), threshold)
        big_matrix.db_rep.save_on_begin_rand(matrix)
        return big_matrix

    def convert_sparse_to_bigmatrix(self,
                                    sparce_matrix: csc_matrix,
                                    threshold: int) -> BigMatrix:
        n = sparce_matrix.shape[0]

        big_matrix = BigMatrix(self.name, n, threshold)
        big_matrix.db_rep.save_sparse_on_begin(sparce_matrix)
        return big_matrix

    def create_bigmatrix_from_lines(self, lines, name="test", threshold: int = 5) -> BigMatrix:
        ...
        big_matrix = BigMatrix(self.name, len(lines), threshold)
        big_matrix.db_rep.save_on_begin_rand(lines)
        return big_matrix


def convert_small_to_big(matrix, name='test', threshold=50):
    big_matrix = BigMatrixConverter(
        name
    ).convert_small_to_bigmatrix(matrix, threshold)
    # inverse_mat = big_matrix.sp_inverse()
    return big_matrix


def test_small_matrix():
    from inverse import close_identity
    threshold = 500
    matrix = np.array([[19, 2, 3],
                       [8, 3, 6],
                       [7, 8, 15]])
    big_matrix = BigMatrixConverter(
        "test").convert_small_to_bigmatrix(matrix, threshold)
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
