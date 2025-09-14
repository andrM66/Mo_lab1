import numpy as np


N = 200


def make_A_matrix(B: np.ndarray) -> np.ndarray:
    """
    Расчет матрицы A
    :param B: ковариационная матрица
    :return: Матрицу A
    """
    A = np.zeros_like(B, dtype=np.float32)
    a,b = A.shape
    for i in range(a):
        for j in range(b):
            if i == j:
                tmp_a_sum = 0
                for k in range(i):
                    tmp_a_sum += A[i, k] ** 2
                if i == 0:
                    A[i, i] = np.sqrt(B[i, i])
                else:
                    A[i, i] = np.sqrt(B[i,i] - tmp_a_sum)
            if i < j:
                if i == 0:
                    A[j, i] = B[0, j] / A[0, 0]
                else:
                    tmp_a_sum = 0
                    for k in range(i):
                        tmp_a_sum += A[i, k] * A[j, k]
                    A[j, i] = (B[i, j] - tmp_a_sum)/A[i, i]
    return A


def gen_norm_vector(A: np.ndarray, M: np.ndarray) -> np.ndarray:
    """
    Генерация случайного вектора на основе полученной матрицы A
    :param A:
    :param M: вектор мат ожиданий
    :return: Случайный вектор
    """
    a, b = A.shape
    E = np.zeros(a, dtype=np.float32)
    for i in range(a):
        E = np.random.normal(0, 1, 2)
    X = A.dot(E) + M
    return X


def gen_sample(volume: int, M: np.ndarray, B: np.ndarray, filename: str = None):
    """
    На основе входных данных генерирует выборку из N случайных векторов
    :param volume: объем выборки
    :param M: вектор мат ожиданий
    :param B: ковариационная матрица
    :param filename: файл для сохранения выборки
    :return: None
    """
    A = make_A_matrix(B)
    X = []
    for i in range(volume):
        X.append(gen_norm_vector(A, M))
    result = np.vstack((X[0], X[1]))
    for i in range(2, volume):
        result = np.vstack((result, X[i]))
    if filename is not None:
        np.save(filename, result)


