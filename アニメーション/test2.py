# -*- coding: utf-8 -*-
"""
matplotlibでリアルタイムプロットする例

無限にsin関数をplotし続ける
"""
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt


def pause_plot():
    fig, ax = plt.subplots(1, 1)
    x = np.arange(-3*np.pi, 3*np.pi, 0.4)
    y = np.sinc(x)
    # 初期化的に一度plotしなければならない
    # そのときplotしたオブジェクトを受け取る受け取る必要がある．
    # listが返ってくるので，注意
    lines, = ax.plot(x, y, marker="o", ls="", ms=10, mfc="white", mec="C0")

    ax.set_xlim((x.min(), x.max()))

    # ここから無限にplotする
    x_left_lim = 0
    while True:
        x_left_lim = (x_left_lim % len(x)) + 1
        set_x = x[:x_left_lim]

        lines.set_data(set_x, np.sinc(set_x))

        plt.pause(.05)


if __name__ == "__main__":
    pause_plot()
