from lyapunov_solver import *
from models import *


def tune(alpha, beta, A, Q, x0, a_x, a_y, x_start, y_start,  b_x, b_y, time, freq):
    rows_a, cols_a = a_x.shape
    rows_b, cols_b = b_x.shape

    P = solve_lyapunov(A, Q, x0, time, freq)

    x_model = lambda z, t: basic_model(z, t, a_x)
    y_model = lambda z, t: basic_model(z, t, a_y)

    x = odeint(x_model, x_start, time)
    y = odeint(y_model, y_start, time)
    err = y-x

    a_model = lambda z, t: identification_model_a(z, t, alpha, P, err)
    b_model = lambda z, t: identification_model_a(z, t, beta, P, err)

    delta_a = a_y - a_x
    delta_b = a_y - b_x

    a = odeint(a_model, delta_a.flatten(), time)
    b = odeint(b_model, delta_b.flatten(), time)

    return a.reshape(rows_a, cols_a), b.reshape(rows_b, cols_b)


