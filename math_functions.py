import numpy as np


##----##----##----##----##----##----##----##----##----##


def make_matrix_A(data_x):
    matrix = [[0, 0], [0, 0]]
    matrix[0][0] = len(data_x)
    matrix[0][1] = sum(data_x)
    matrix[1][0] = matrix[0][1]
    matrix[1][1] = sum(x**2 for x in data_x)
    return matrix


def determiner(data_x):
    a = make_matrix_A(data_x)
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def determiner_alpha(data_x, data_y):
    res = sum(x**2 for x in data_x) * sum(data_y)
    res -= sum(data_x) * sum(z[0] * z[1] for z in zip(data_x, data_y))
    return res


def determiner_beta(data_x, data_y):
    res = len(data_x) * sum(z[0] * z[1] for z in zip(data_x, data_y))
    res -= sum(data_x) * sum(data_y)
    return res


def coefficients(data_x, data_y):
    d = determiner(data_x)
    alpha = determiner_alpha(data_x, data_y) / d
    beta = determiner_beta(data_x, data_y) / d
    return alpha, beta


def k(data_x, data_y):
    sum = 0
    avg_x = np.average(data_x)
    avg_y = np.average(data_y)
    for i in range(0, len(data_x)):
        sum += (data_x[i] - avg_x) * (data_y[i] - avg_y)
    return sum / len(data_x)


def s(data):
    #return np.std(np.array(data))
    s1 = sum(data)
    s2 = sum([d**2 for d in data])
    return np.sqrt(s2 / len(data) - (s1 / len(data))**2)


def rxy(data_x, data_y):
    kVal = k(data_x, data_y)
    sx = s(data_x)
    sy = s(data_y)
    return kVal / (sx * sy)


def r_y_on_x(data_x, data_y):
    rxyVal = rxy(data_x, data_y)
    sy = s(data_y)
    sx = s(data_x)
    return rxyVal * (sy / sx)


def r_x_on_y(data_x, data_y):
    return rxy(data_x, data_y) * (s(data_x) / s(data_y))