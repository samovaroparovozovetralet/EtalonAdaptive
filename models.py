import numpy as np


def basic_model(z, t, a):
    return a @ z


def basic_control_model(z, t, a, b, u):
    return a @ z + b @ u


def coordination_conditions_model(z, t, a, b, c, y, f, freq):
    index_y_access = int(t * freq - 1)
    if index_y_access < len(y):
        return (a + b @ c) @ z + b @ f @ z - b @ c @ y[index_y_access]
    else:
        return (a + b @ c) @ z + b @ f @ z - b @ c @ y[-1]


def equal_matrix_model(z, t, a, b, c, y, freq):
    index_y_access = int(t * freq - 1)
    if index_y_access < len(y):
        return (a + b @ c) @ z - b @ c @ y[index_y_access]
    else:
        return (a + b @ c) @ z - b @ c @ y[-1]


def identification_model_a(z, t, alpha, p, err):
    a = np.zeros_like(alpha)
    rows, cols = alpha.shape
    print(p[:, 0] @ err)
    for i in range(rows):
        for j in range(cols):
            a[i, j] = -alpha[i, j] * p[:, i] @ err

    return a.flatten()


def identification_model_b(z, t, beta, p, err):
    b = np.zeros_like(beta)
    rows, cols = beta.shape
    for i in range(rows):
        for j in range(cols):
            b[i, j] = -beta[i, j] * p[:, i] @ err

    return b.flatten()

