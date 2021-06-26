import numpy as np


class ode_basic:
    a = []
    b = []
    freq = 100
    time = np.arange(0, 1.0, 1.0/freq)
    start_model = []
    start_exp = []
    roots = []

    def __init__(self, a, b, freq, time, start_model, start_exp, roots):
        self.a, self.b, self.freq, self.time, self.start_model, self.start_exp, self.roots = a, b, freq, time, start_model, start_exp, roots
