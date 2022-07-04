
class Printer:

    def __init__(self):
        self.__precision = 7
        self.separator = " : "


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, n):
        self.__precision = n if n >= 0 else 0

    @property
    def separator(self):
        return self.__separator

    @separator.setter
    def separator(self, s):
        self.__separator = s


    def number(self, name, value):
        pattern = "{:." + str(self.precision) + "f}"
        print(name, self.separator, pattern.format(value))


    def matrix(self, name, matrix):
        pattern = "{:.4f}"
        print(name, self.separator)
        for row in matrix:
            print("    ", end="")
            for elem in row:
                print(pattern.format(elem), end=" ")
            print()


    def text(self, name, text):
        print(name, self.separator, text)
