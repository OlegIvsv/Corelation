import src.data_reading as dr
import src.smaller_squares_method as ssm
import src.static_coefficient_method as scm

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
    ssm.method_of_smaller_squares(data_x, data_y)
    print()
    print("Використовуємо метод статичного коефіцієнта кореляції" + "-*" * 30)
    scm.method_of_stat_coef(data_x, data_y)

##----##----##----##----##----##----##----##----##----##

main()
