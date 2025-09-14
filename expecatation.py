import numpy as np


def gen_A_matrix(B: np.ndarray) -> np.ndarray:
    '''
    Zалупа
    :param M:
    :param B:
    :return:
    '''
    A = np.zeros_like(B)
    a,b = A.shape # a -- строчки b -- стобцы
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
    '''

    :param A:
    :param M:
    :return:
    '''
    a, b = A.shape
    E = np.zeros(a)
    for i in range(a):
        tmp = np.random.normal(0, 1, 1)
        E[i] = tmp[0]
    E = E.transpose()
    X = A.dot(E) + M.transpose()
    return X



if __name__ == '__main__':
    M = np.array([1, 1, 1])
    B = np.array([[1,2, 3], [3,4, 2], [2,1,4]])
    A = gen_A_matrix(B)
    print(A)
    X = gen_norm_vector(A, M)
    print(X)
