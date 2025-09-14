import numpy as np
from expecatation import gen_sample


N = 200


if __name__ == '__main__':
    M1 = np.array([2, 3])
    M2 = np.array([6, 5])
    B = np.array([[1.5, 0.9], [0.9, 1.5]])
    gen_sample(N, M1, B, "X1")
    gen_sample(N, M2, B, "X2")