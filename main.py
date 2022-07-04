import math_functions as mf
from printer import Printer
import numpy as np
import charting
import data_reading as dr

##----##----##----##----##----##----##----##----##----##

RESULTS_COLOUR = "\033[1;35;40m"
USUAL_COLOUR = "\033[1;36;40m"
DATA_X_DEFAULT = [0.32, 0.34, 0.34, 0.49, 0.52, 0.81, 0.88, 0.57, 0.42, 0.25, 0.86, 0.99, 0.72, 0.43, 0.25, 0.78, 0.29, \
                  0.35, 0.34, 0.42, 0.47, 0.60, 0.34, 0.49, 0.91, 0.24, 0.32, 0.34, 0.41, 0.57, 0.86, 0.99]
DATA_Y_DEFAULT = [0.29, 0.31, 0.65, 0.76, 0.43, 0.32, 0.10, 0.00, 0.34, 0.10, 0.00, 0.02, 0.22, 0.29, 0.31, 0.43, 0.24, \
                  0.32, 0.35, 0.43, 0.62, 0.81, 0.43, 0.27, 0.99, 0.59, 0.43, 0.23, 0.12, 0.24, 0.65, 0.76]


def main():
    print(USUAL_COLOUR)

    data_x = dr.read_array("Дані X : ", DATA_X_DEFAULT, " ")
    data_y = dr.read_array("Дані Y : ", DATA_Y_DEFAULT, " ")

    print("Використовуємо метод найменших квадратів" + "-*" * 30)
    method_of_smaller_squares(data_x, data_y)
    print()
    print("Використовуємо метод статичного коефіцієнта кореляції" + "-*" * 30)
    method_of_stat_coef(data_x, data_y)

# M E T H O D   O F   T H E   S T A T I C   C O E F F I C I E N T

def method_of_stat_coef(data_x, data_y):

    print_y_on_x_stat_coef(data_x, data_y)
    print("*" * 45)
    print_x_on_y_stat_coef(data_x, data_y)
    build_chart_for_stat_coef(data_x, data_y)


def build_chart_for_stat_coef(data_x, data_y):

    avg_x = np.average(data_x)
    avg_y = np.average(data_y)
    r_y_on_x = mf.r_y_on_x(data_x, data_y)
    r_x_on_y = mf.r_x_on_y(data_x, data_y)

    max_x = max(data_x) * 1.15
    line1_xs = [0, max_x]
    line1_ys = [avg_y + r_y_on_x * (0 - avg_x), avg_y + r_y_on_x * (max_x - avg_x)]
    y_label = "y = {:.4f} + {:.4f} * (x* - {:4f})".format(avg_y, r_y_on_x, avg_x)

    max_y = max(data_y) * 1.25
    line2_ys = [0, max_y]
    line2_xs = [avg_x + r_x_on_y * (0 - avg_y), avg_x + r_x_on_y * (max_y - avg_y)]
    x_label = "x = {:.4f} + {:.4f} * (y* - {:.4f})".format(avg_x, r_x_on_y, avg_y)

    charting.build_charts('', data_x, data_y, line1_xs, line1_ys, line2_xs, line2_ys, ["Дані", y_label, x_label])


def print_x_on_y_stat_coef(data_x, data_y):
    printer = Printer()
    printer.precision = 5

    avg_x = np.average(data_x)
    avg_y = np.average(data_y)
    r_x_on_y = mf.r_x_on_y(data_x, data_y)

    printer.number("rxy", mf.rxy(data_x, data_y))
    printer.number("Середнє x", avg_x)
    printer.number("S0x", mf.s(data_x))
    printer.number("r x|y", r_x_on_y)

    x_string = "x* - {:.5f} = {:.5f}(y* - {:.5f})"
    print(RESULTS_COLOUR + x_string.format(avg_x, r_x_on_y, avg_y) + USUAL_COLOUR)


def print_y_on_x_stat_coef(data_x, data_y):
    printer = Printer()
    printer.precision = 5
    printer.separator = " = "

    avg_x = np.average(data_x)
    avg_y = np.average(data_y)
    r_y_on_x = mf.r_y_on_x(data_x, data_y)

    printer.number("rxy", mf.rxy(data_x, data_y))
    printer.number("Середнє y", avg_y)
    printer.number("S0y", mf.s(data_y))
    printer.number("r y|x", r_y_on_x)

    x_string = "y* - {:.5f} = {:.5f}(x* - {:.5f})"
    print(RESULTS_COLOUR + x_string.format(avg_y, r_y_on_x, avg_x) + USUAL_COLOUR)

# M E T H O D   O F   T H E   S M A L L E R   S Q U A R E S
def method_of_smaller_squares(data_x, data_y):
    print_y_on_x_smaller_squares(data_x, data_y)
    print("*" * 45)
    print_x_on_y_smaller_squares(data_x, data_y)
    build_chart_for_smaller_squares(data_x, data_y)


def build_chart_for_smaller_squares(data_x, data_y):

    alpha, beta = mf.coefficients(data_x, data_y)
    max_x = max(data_x) * 1.15
    line1_xs = [0, max_x]
    line1_ys = [alpha +  beta * 0, alpha + beta * max_x]
    y_label = "y ={:.4f}  + {:.4f} * x*".format(alpha, beta)

    alpha, beta = mf.coefficients(data_y, data_x)
    max_y = max(data_y) * 1.25
    line2_ys = [0, max_y]
    line2_xs = [alpha + beta * 0, alpha + beta * max_y]
    x_label = "x ={:.4f}  + {:.4f} * y*".format(alpha, beta)

    charting.build_charts('', data_x, data_y,
        line1_xs, line1_ys, line2_xs, line2_ys, ("Дані", y_label, x_label))


def print_y_on_x_smaller_squares(data_x, data_y):
    printer = Printer()
    printer.precision = 5

    printer.matrix("A", mf.make_matrix_A(data_x))

    printer.separator = " = "
    printer.number("∆", mf.determiner(data_x))
    printer.number("∆𝛼", mf.determiner_alpha(data_x, data_y))
    printer.number("∆𝛽", mf.determiner_beta(data_x, data_y))

    alpha, beta = mf.coefficients(data_x, data_y)
    printer.number("𝛼", alpha)
    printer.number("𝛽", beta)

    y_string = f"y* = {round(alpha, 5)} + {round(beta, 5)}x*"
    print(RESULTS_COLOUR + y_string + USUAL_COLOUR)


def print_x_on_y_smaller_squares(data_x, data_y):
    printer = Printer()
    printer.precision = 5

    printer.matrix("A'", mf.make_matrix_A(data_y))

    printer.separator = " = "
    printer.number("∆'", mf.determiner(data_y))
    printer.number("∆𝛼'", mf.determiner_alpha(data_y, data_x))
    printer.number("∆𝛽'", mf.determiner_beta(data_y, data_x))

    alpha, beta = mf.coefficients(data_y, data_x)
    printer.number("𝛼", alpha)
    printer.number("𝛽", beta)

    x_string = f"x* = {round(alpha, 5)} + {round(beta, 5)}y*"
    print(RESULTS_COLOUR + x_string + USUAL_COLOUR)



##----##----##----##----##----##----##----##----##----##

main()

"""
0.25 0.31 0.36 0.65 0.65 0.70 0.03 0.28 0.33 0.57 0.38 0.78 0.35 0.38 0.42 0.47 0.91 0.89 0.49 0.60 0.86 0.99 0.72 0.43

0.15 0.36 0.30 0.56 0.65 0.62 0.24 0.29 0.52 0.36 0.68 0.76 0.24 0.32 0.35 0.43 0.62 0.81 0.99 0.59 0.43 0.27 0.32 0.29
"""