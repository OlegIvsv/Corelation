import matplotlib.pyplot as plt

##----##----##----##----##----##----##----##----##----##

def build_charts(title, points_xs, points_ys, line1_xs, line1_ys, line2_xs, line2_ys, labels):

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)

    plt.plot(points_xs, points_ys, "o", label=labels[0])
    plt.plot(line1_xs, line1_ys, label=labels[1])
    plt.plot(line2_xs, line2_ys, label=labels[2])
    plt.legend(labels, loc="upper right")
    plt.show()














