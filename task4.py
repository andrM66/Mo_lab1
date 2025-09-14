import numpy as np


N = 200


def find_params(X: np.ndarray, N: int) -> tuple:
    """
    Нахождение оценок параметров
    :param X:
    :param N:
    :return:
    """
    a, b = X.shape
    M = np.zeros(b, dtype=np.float32)
    for i in range(b):
        M[i] = np.sum(X[:, i]) / N
    B = np.zeros((b, b) , dtype=np.float32)
    for i in range(b):
        for j in range(b):
            tmp_x = (X[:, i] - M[i]) * (X[: , j]- M[j])
            tmp_x = np.sum(tmp_x) / N
            B[i, j] = tmp_x
    return B, M



if __name__ == '__main__':
    X1 = np.load("X1.npy")
    X2 = np.load("X2.npy")
    X3 = np.load("task_3_X1.npy")
    X4 = np.load("task_3_X2.npy")
    X5 = np.load("task_3_X3.npy")
    B1, M1 = find_params(X1, N)
    B2, M2 = find_params(X2, N)
    B3, M3 = find_params(X3, N)
    B4, M4 = find_params(X4, N)
    B5, M5 = find_params(X5, N)
    print(f'M1 = {M1}, M2 = {M2} \n B(task2) = {B1}\n B(task2 var 2) = {B2}\n')
    print(f'M1(task3) = {M3}, B1(task3) = {B3}')
    print(f'M1(task3) = {M4}, B1(task3) = {B4}')
    print(f'M1(task3) = {M5}, B1(task3) = {B5}')

