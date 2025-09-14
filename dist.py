import numpy as np
import numpy.linalg


def find_mahalo_dist(M0:np.ndarray, M1: np.ndarray, B: np.ndarray) -> np.float32:
    """
    :param M0:
    :param M1:
    :param B:
    :return:
    """
    rho = np.dot((M0 - M1).T, np.linalg.inv(B))
    rho = np.dot(rho, (M1-M0))
    return rho


def find_baha_dist(M0: np.ndarray, M1: np.ndarray, B0: np.ndarray, B1: np.ndarray) -> np.float32:
    """
    :param M0:
    :param M1:
    :param B0:
    :param B1:
    :return:
    """
    rho = 1/4 * np.dot((M1 - M0).T, np.linalg.inv((B1 + B0)/2))
    rho = np.dot(rho, (M1 - M0)) + 0.5 * np.log(np.linalg.det((B1+B0)/2)/np.sqrt(np.linalg.det(B1) * np.linalg.det(B0)))
    return rho


if __name__ == "__main__":
    M1 = np.array([2, 3])
    M2 = np.array([6, 5])
    B = np.array([[1.5, 0.9], [0.9, 1.5]])
    print(find_mahalo_dist(M1, M2, B))

    M3 = np.array([2, 2])
    M4 = np.array([6, 7])
    M5 = np.array([9, 3])
    B3 = np.array([[0.3, 0.1], [0.1, 0.4]])
    B4 = np.array([[2.0, 1.8], [1.8, 2.0]])
    B5 = np.array([[1.5, -1.2], [-1.2, 1.0]])
    print(find_baha_dist(M3, M4, B3, B4))