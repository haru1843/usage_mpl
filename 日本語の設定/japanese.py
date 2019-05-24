import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl


def main():
    font = {"family": "IPAexGothic"}
    mpl.rc('font', **font)

    x_num = 200
    x = np.linspace(0, 100, num=x_num)
    y = (0.1*x*x + 2*x + 3) +\
         np.random.normal(0, 150, x_num) +\
         np.random.normal(0, 40, x_num)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, label='実験値')

    p = np.polyfit(x, y, 2)
    ax.plot(x, p[0]*x*x + p[1]*x + p[2], label='最小二乗法')

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlabel('時間$t$ [$\\rm ms$]')
    ax.set_ylabel('温度変化 [$\\rm ^{\circ}C$]')

    ax.legend()

    plt.show()


if __name__ == '__main__':
    main()