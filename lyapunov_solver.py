from scipy.integrate import odeint
import numpy as np


def solve_lyapunov(A, Q, x0, time, freq):

    rows, cols, _ = A.shape

    def right(y, t):
        X = np.reshape(y, (rows, cols))
        return -(np.tensordot(X, A, (0, 1)) + np.tensordot(X, np.transpose(A, (1, 0, 2)), (0, 1)) + Q).reshape(rows*cols, freq)[:, int(t*(freq - 1))]

    P = odeint(right, x0, time)
    P = np.reshape(P, (rows, cols, freq))

    return P

