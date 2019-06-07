import matplotlib.pyplot as plt
import numpy as np


def main():
    try_num = 5000
    x_list = np.array([0] * try_num)
    y_list = np.array([0] * try_num)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for loop_num in range(10):

        for i in range(try_num-1):
            x_list[i+1] = x_list[i] + np.random.choice([-1, 1])
            y_list[i+1] = y_list[i] + np.random.choice([-1, 1])

        ax.plot(x_list, y_list,
                label=str(loop_num*try_num+1) + "~" + str((loop_num+1)*try_num))
        x_list[0] = x_list[-1]
        y_list[0] = y_list[-1]

    ax.legend(fontsize=6)
    # plt.show()
    plt.savefig("random_walk.svg", format="svg")


if __name__ == '__main__':
    main()
