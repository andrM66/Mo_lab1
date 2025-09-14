import numpy as np


N = 200


def make_A_matrix(B: np.ndarray) -> np.ndarray:
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
    X = A.dot(E) + M.transpose()
    return X


def gen_sample(volume: int, M: np.ndarray, B: np.ndarray) -> np.ndarray:
    '''

    :param volume:
    :param M:
    :param B:
    :return:
    '''
    A = make_A_matrix(B)
    X = []
    for i in range(volume):
        X.append(gen_norm_vector(A, M))
    result = np.vstack((X[0], X[1]))
    for i in range(2, volume):
        result = np.vstack((result, X[i]))
    return  result

if __name__ == '__main__':
    M1 = np.array([2, 3])
    M2 = np.array([6, 5])
    B = np.array([[1.5, 0.9], [0.9, 1.5]])
    X1 = gen_sample(N, M1, B)
    print(X1)


