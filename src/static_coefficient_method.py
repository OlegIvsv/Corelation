from src.printer import Printer
import src.math_functions as mf
import src.charting as charting
import numpy as np

##----##----##----##----##----##----##----##----##----##

RESULTS_COLOUR = "\033[1;35;40m"
USUAL_COLOUR = "\033[1;36;40m"

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