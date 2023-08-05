import numpy as np
from inverse import get_matrix_for_test

from inverse.src.matrix_converters import BigMatrixConverter
from inverse.src.sp_matrix_ops import display_matrix_ozet
from inverse.src.sp_utils_inverse import close_identity
from inverse.src.sure import tic, toc


def inverse_random_matrix(n=10, threshold=50):
    from inverse.src.check_result import inverse_check

    matrix = get_matrix_for_test(n)
    print(matrix)
    matrix_check = inverse_check(matrix)
    converter = BigMatrixConverter("test")
    big_matrix = converter.convert_small_to_bigmatrix(matrix, threshold=threshold)  # class bigMatrix
    tic()
    inv_big_matrix = big_matrix.sp_inverse()  # class bigMatrix
    toc()
    display_matrix_ozet(inv_big_matrix, "inv_big_matrix")
    display_matrix_ozet(inv_big_matrix, "inv_big_matrix main")
    display_matrix_ozet(matrix_check, "matrix_check")
    sonuc = np.matmul(matrix, inv_big_matrix)
    sonuc2 = np.matmul(matrix, matrix_check)
    display_matrix_ozet(sonuc, "sonuc A * A(-1)")
    display_matrix_ozet(sonuc2, "sonuc2 matrix_check A * A(-1)")
    eps = 0.0001
    kontrol = close_identity(matrix=sonuc, eps=eps)
    kontrol2 = close_identity(matrix=sonuc2, eps=eps)


from inverse.ctypes_loc.cdeneme import test_c

# __all__ = ["inverse_random_matrix", "test_c"]
