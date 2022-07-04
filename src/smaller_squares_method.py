from src.printer import Printer
import src.math_functions as mf
import src.charting as charting
import numpy as np

##----##----##----##----##----##----##----##----##----##

RESULTS_COLOUR = "\033[1;35;40m"
USUAL_COLOUR = "\033[1;36;40m"

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