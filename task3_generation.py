import numpy as np
from expecatation import gen_sample


N = 200


if __name__ == '__main__':
    M1 = np.array([2, 2])
    M2 = np.array([6, 7])
    M3 = np.array([9, 3])
    B1 = np.array([[0.3, 0.1], [0.1, 0.4]])
    B2 = np.array([[2.0, 1.8], [1.8, 2.0]])
    B3 = np.array([[1.5, -1.2], [-1.2, 1.0]])
    gen_sample(N, M1, B1, "task_3_X1")
    gen_sample(N, M2, B2, "task_3_X2")
    gen_sample(N, M3, B3, "task_3_X3")