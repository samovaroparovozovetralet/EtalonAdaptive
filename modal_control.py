import numpy as np


class EugeneStabilisation:
    a = []
    b = []
    rows, cols = 1, 1

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.rows, self.cols = a.shape

    #
    def find_s(self):
        curr_matrix = np.eye(self.rows)
        s = curr_matrix @ self.b
        for i in range(1, self.rows):
            curr_matrix = curr_matrix @ self.a
            s = np.append(s, curr_matrix @ self.b, axis=1)
        return np.array(s)

    # find A**n decomposition coefficients
    def find_p(self):
        return -np.flip(np.linalg.pinv(self.find_s()) @ np.linalg.matrix_power(self.a, self.rows) @ self.b)

    def find_u_from_a(self, a):
        p = self.find_p()
        s = self.find_s()
        p_diagonal = np.eye(self.rows)
        for i in range(self.rows - 1):
            p_diagonal += np.eye(self.rows, k=i+1) * p[i]

        return np.conjugate(p.T - a) @ np.linalg.pinv(p_diagonal) @ np.linalg.pinv(s)

    def find_u_from_roots(self, roots):
        poly = np.poly(roots)
        return self.find_u_from_a(poly[1:])
