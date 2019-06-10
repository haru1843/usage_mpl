import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def positive_circ(x):
    # 正の円弧を算出
    return np.sqrt(1 - x*x)


def main():
    font = {"family": "IPAexGothic"}
    mpl.rc('font', **font)

    point_num = 500
    loop_num = 8
    point_in_circ_num = 0

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)

    for i in range(loop_num):
        x_list = np.random.rand(point_num)
        y_list = np.random.rand(point_num)

        # 各点の距離の二乗を算出
        distance_list = x_list ** 2 + y_list ** 2

        # 各点の内, 距離の二乗が1に満たないものの個数を集める
        point_in_circ_num += np.sum(distance_list <= 1)

        # 円周率の推定
        est_pi = 4*point_in_circ_num/((i+1)*point_num)

        # 散布図
        ax.scatter(x_list, y_list,
                   label="{}回目 : {:2.6}".format(i+1, est_pi), s=3)

    # 円弧の描画
    x = np.linspace(0, 1, 3000)
    y = positive_circ(x)
    ax.plot(x, y, color="black", zorder=100)

    # 描画範囲の指定
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])

    # 凡例の表示
    ax.legend()
    plt.savefig("monte_carlo.svg", format="svg")


if __name__ == '__main__':
    main()
