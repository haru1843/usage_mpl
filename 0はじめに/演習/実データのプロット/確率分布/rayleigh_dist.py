import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import re
import math

def rayleigh_dist(x, s2):
    return x*np.exp(x**2/(-2*s2))/s2

def sum_rayleigh_dist(x, s2):
    return 1 - np.exp(x**2/(-2*s2))

def main():
    font = {"family": "IPAexGothic"}
    mpl.rc('font', **font)

    x = np.arange(0, 10.001, 0.02)
    s_list = [0.5, 1.0, 2.0, 3.0, 4.0]

    fig = plt.figure()

    # -- 密度関数の描画 --
    ax = fig.add_subplot(111)
    for s in s_list:
        ax.plot(x, rayleigh_dist(x, s**2), label='$\sigma = {}$'.format(s))

    ax.set_xlim([0, 10])
    ax.set_ylim([0, 1.25])
    ax.set_xlabel("x")
    ax.set_ylabel("$f(x)$")
    ax.set_title("レイリー分布の確率密度関数")
    ax.legend()
    ax.grid()

    # -- pdfの作成 --
    plt.savefig(re.sub(".py", "", os.path.basename(__file__))+".png")



    # -- 分布関数の描画 --
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for s in s_list:
        ax.plot(x, sum_rayleigh_dist(x, s**2), label='$\sigma = {}$'.format(s))

    ax.set_xlim([0, 10])
    ax.set_ylim([0, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("$F(x)$")
    ax.set_title("レイリー分布の確率分布関数")
    ax.legend()
    ax.grid()

    # -- pdfの作成 --
    plt.savefig(re.sub(".py", "", os.path.basename(__file__))+"_sum.png")

if __name__ == "__main__":
    main()
