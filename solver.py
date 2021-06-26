from modal_control import EugeneStabilisation
from scipy.integrate import odeint
from models import *
from scipy.linalg import pinv


def solve_equal_matrix_problem(a, b, time, start_model, start_exp, freq, roots, u_test=0):
    ex_p = EugeneStabilisation(a, b)
    c = ex_p.find_u_from_roots(roots)

    y_basic_model = lambda z, t: basic_model(z, t, a)

    y_m = odeint(y_basic_model, start_model, time)
    y_p = odeint(y_basic_model, start_exp, time)

    stabilized_model = lambda z, t: equal_matrix_model(z, t, a, b, c, y_m, freq)

    y_stabilized = odeint(stabilized_model, start_exp, time)
    err = y_stabilized - y_m

    return y_m, y_p, y_stabilized, err


def solve_coordination_cond_problem(a_m, b_m, a_p, b_p, u_test, time, start_model, start_exp, freq, roots):
    ex = EugeneStabilisation(a_m, b_p)
    c = ex.find_u_from_roots(roots)

    b_inv = pinv(b_p)
    del_a = a_m - a_p
    f = b_inv @ del_a
    q = b_inv @ b_m

    y_m_model = lambda z, t: basic_model(z, t, a_m)
    y_p_model = lambda z, t: basic_model(z, t, a_p)

    y_m = odeint(y_m_model, start_model, time)
    y_p = odeint(y_p_model, start_exp, time)

    stabilized_model = lambda z, t: coordination_conditions_model(z, t, a_m, b_p, c, y_m, f, freq)

    y_stabilized = odeint(stabilized_model, start_exp, time)
    err = y_stabilized - y_m

    return y_m, y_p, y_stabilized, err

