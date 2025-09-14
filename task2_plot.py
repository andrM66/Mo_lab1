import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    X1 = np.load("X1.npy")
    X2 = np.load("X2.npy")
    plt.plot(X1[:, 0], X1[:, 1], color='red', marker='.', linestyle='none')
    plt.plot(X2[:, 0], X2[:, 1], color='blue', marker="+", linestyle="none")
    plt.show()