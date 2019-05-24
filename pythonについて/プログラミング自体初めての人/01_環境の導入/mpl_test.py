import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl


def main():
    font = {"family": "Yu Gothic"}
    mpl.rc('font', **font)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # あるべき曲線
    x_lim = [0, 3]
    x = np.linspace(*x_lim, 300)
    y = 2*(x**2) + 4*x + 3
    ax.plot(x, y, label="本来", color="C0")

    # 実験値の描画
    y += np.random.normal(1, 5, len(x)) + np.random.normal(-1, 2, len(x))
    ax.plot(x, y, label="実験値", alpha=0.4, color="C2")

    # 最小二乗法の描画
    p = np.polyfit(x, y, 2)
    y = p[0]*(x**2) + p[1]*x + p[2]
    ax.plot(x, y, label="最小二乗法", color="C1")

    # 図の設定
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(x_lim)
    ax.legend()

    # 図の表示
    plt.show()


if __name__ == '__main__':
    main()