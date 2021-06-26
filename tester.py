from matplotlib import pyplot as plt
from solver import *
from identification_solver import *
import pandas as pd

"""
A = np.array(
    [[t, np.zeros_like(t)],
     [np.zeros_like(t), t]],
    dtype=float
)

Q = np.array(
    [[np.exp(-t), np.zeros_like(t)],
     [np.zeros_like(t), np.exp(-t)]],
    dtype=float
)

x0 = [1, 1, 1, 1]

in_sec = 100
time = np.arange(0, 1.0, 1.0/in_sec)
    
"""


def single_test_equal_matrix(a, b, time, freq, start_model, start_exp, roots):

    y_m, y_p, y, err = solve_equal_matrix_problem(a, b, time, start_model, start_exp, freq, roots)

    plt.plot(y_m[:, 0], 'r', y[:, 0], 'b')
    plt.show()
    return y_m, y_p, y, err


def mult_test_equal_matrix(objects_list):
    for item in objects_list:
        y_m, y_p, y, err = solve_equal_matrix_problem(item.a, item.b, item.time, item.start_model, item.start_exp, item.freq, item.roots)

        plt.plot(y_m[:, 0], 'r', y[:, 0], 'b')
        plt.show()


def single_test_coordination_cond(a_m, b_m, a_p, b_p, time, freq, start_model, start_exp, roots):
    u_test = np.zeros_like(b_m)
    y_m, y_p, y, err = solve_coordination_cond_problem(a_m, b_m, a_p, b_p, u_test, time, start_model, start_exp, freq, roots)

    plt.plot(y_m[:, 2], 'r', y[:, 2], 'b')
    plt.show()
    return y_m, y_p, y, err


def mult_test_coordination_condition(objects_list):
    for item in objects_list:
        y_m, y_p, y, err = solve_coordination_cond_problem(item.a, item.b, item.time, item.start_model, item.start_exp, item.freq, item.roots)

        plt.plot(y_m[:, 0], 'r', y[:, 0], 'b')
        plt.show()


def test_identification(alpha, beta, A, Q, q0, a_x, a_y, x_start, y_start, b_x, b_y, time, freq):

    a, b = tune(alpha, beta, A, Q, q0, a_x, a_y, x_start, y_start, b_x, b_y, time, freq)

    a_p_tuned = a + a_x
    b_p_tuned = b + b_x
    u = np.zeros_like(b_y)

    y_model = lambda z, t: basic_control_model(z, t, a_y, b_y, u)
    y_x_model = lambda z, t: basic_model(z, t, a_p_tuned)

    y = odeint(y_model, y_start, time)
    x = odeint(y_x_model, x_start, time)

    plt.plot(x[:, 0], 'r', y[:, 0], 'b')
    plt.show()


def save_csv(y_m, y_stabilized, time, marker):
    rows, cols = y_m.shape
    for i in range(cols):
        plot_table = pd.DataFrame(np.array((y_m[:, i], y_stabilized[:, i], time)).T, columns=("model", "stabilized", "time"))
        plot_table.to_csv(path_or_buf="tables/matrix_table_" + marker + str(i) + ".csv", index=False)
