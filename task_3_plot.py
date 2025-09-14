import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    X1 = np.load("task_3_X1.npy")
    X2 = np.load("task_3_X2.npy")
    X3 = np.load("task_3_X3.npy")
    plt.plot(X1[:, 0], X1[:, 1], color='red', marker='.', linestyle='none')
    plt.plot(X2[:, 0], X2[:, 1], color='blue', marker="+", linestyle="none")
    plt.plot(X3[:, 0], X3[:, 1], color='green', marker="*", linestyle="none")
    plt.show()