import numpy as np
import pandas as pd

standard_time = np.arange(0, 1.0, 1.0/100.0)

basic_set_equal_matrix = {"a": pd.read_csv("system_matrix/matrix_template.csv", header=None).to_numpy(),
                          "b": pd.read_csv("system_matrix/control_matrix_template.csv", header=None).to_numpy(),
                          "freq": 1000,
                          "time": np.arange(0, 1.0, 1.0/1000),
                          "start_model": [1, 1, 1],
                          "start_exp": [2, 2, 2],
                          "roots": [-10, -2, -3]}

equal_matrix_simple = {"a": np.array([[2, 1, 1],
                                      [2, 3, 2],
                                      [3, 3, 4]]),
                       "b": np.vstack([1, 1, 1]),
                       "freq": 10000.0,
                       "time": np.arange(0, 1.0, 1.0/10000.0),
                       "start_model": [1, 1, 1],
                       "start_exp": [2, 100, 250],
                       "roots": [-6, -2, -3]}

smpex_set_coordination_condition = {"a_m": np.array([[2, 1, 1],
                                                     [2, 3, 2],
                                                     [3, 3, 4]]),
                                    "b_m": pd.read_csv("system_matrix/control_matrix_template.csv", header=None).to_numpy(),
                                    "a_p": np.array([[1, 0, 0],
                                                     [0, 1, 0],
                                                     [0, 0, 1]]),
                                    "b_p": pd.read_csv("system_matrix/control_matrix_received.csv", header=None).to_numpy(),
                                    "freq": 100,
                                    "time": np.arange(0, 1.0, 1.0/100.0),
                                    "start_model": [1, 1, 1],
                                    "start_exp": [2, 100, 250],
                                    "roots": [-6, -2, -3]}

basic_set_coordination_condition = {"a_m": pd.read_csv("system_matrix/matrix_template.csv", header=None).to_numpy(),
                                    "b_m": pd.read_csv("system_matrix/control_matrix_template.csv", header=None).to_numpy(),
                                    "a_p": pd.read_csv("system_matrix/matrix_received.txt", header=None).to_numpy(),
                                    "b_p": pd.read_csv("system_matrix/control_matrix_received.csv", header=None).to_numpy(),
                                    "freq": 100,
                                    "time": np.arange(0, 1.0, 1.0/100.0),
                                    "start_model": [1, 1, 1],
                                    "start_exp": [2, 2, 2],
                                    "roots": [-2, -5, -6]}


basic_set_identification = {"a_x": pd.read_csv("system_matrix/matrix_template.csv", header=None).to_numpy(),
                            "b_x": pd.read_csv("system_matrix/control_matrix_template.csv", header=None).to_numpy(),
                            "a_y": pd.read_csv("system_matrix/matrix_received.txt", header=None).to_numpy(),
                            "b_y": pd.read_csv("system_matrix/control_matrix_received.csv", header=None).to_numpy(),
                            "A": np.array(
                                [[-standard_time, np.zeros_like(standard_time), np.zeros_like(standard_time)],
                                 [np.zeros_like(standard_time), -standard_time, np.zeros_like(standard_time)],
                                 [np.zeros_like(standard_time), np.zeros_like(standard_time), -standard_time]],
                                dtype=float
                            ),
                            "Q": np.array(
                                [[np.exp(-standard_time), np.zeros_like(standard_time), np.zeros_like(standard_time)],
                                 [np.zeros_like(standard_time), np.exp(-standard_time), np.zeros_like(standard_time)],
                                 [np.zeros_like(standard_time), np.zeros_like(standard_time), np.exp(-standard_time)]],
                                dtype=float
                            ),
                            "q0": np.ones(9),
                            "alpha": np.ones((3, 3)),
                            "beta": np.ones(3),
                            "freq": 100,
                            "time": np.arange(0, 1.0, 1.0/100.0),
                            "x_start": [1, 1, 1],
                            "y_start": [2, 2, 2],
                            "roots": [-2, -5, -6]}
