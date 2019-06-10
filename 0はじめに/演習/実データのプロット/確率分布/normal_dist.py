import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import re
import math

def normal_dist(x):
    return np.exp(x**2/-2)/np.sqrt(2*np.pi)

def sum_normal_dist(x):
    return [(1+math.erf(x_i/np.sqrt(2)))/2 for x_i in x]

def main():
    font = {"family": "IPAexGothic"}
    mpl.rc('font', **font)

    x = np.arange(-4, 4.001, 0.01)
    mu = 0
    s2 = 1

    fig = plt.figure()

    # -- 密度関数の描画 --
    ax = fig.add_subplot(121)
    ax.plot(x, normal_dist(x))

    ax.set_xlim([-4, 4])
    ax.set_ylim([0, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("$f(x)$")
    ax.set_title("標準正規分布の確率密度関数")
    ax.grid()
    # ax.tight_layout()

    # -- 分布関数の描画 --
    ax = fig.add_subplot(122)
    ax.plot(x, sum_normal_dist(x))

    ax.set_xlim([-4, 4])
    ax.set_ylim([0, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("$F(x)$")
    ax.set_title("標準正規分布の確率分布関数")
    ax.grid()
    plt.tight_layout()

    # -- pdfの作成 --
    plt.savefig(re.sub(".py", "", os.path.basename(__file__))+".png")

    # 合体した図の作成
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, normal_dist(x), color='C0', linestyle='-', alpha=1.0, label='確率密度関数')
    ax.plot(x, sum_normal_dist(x), color='C0', linestyle='--', alpha=0.7, label='確率分布関数')

    ax.set_xlim([-4, 4])
    ax.set_ylim([0, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("$F(x), f(x)$")
    ax.legend()
    ax.grid()

    # -- pdfの作成 --
    plt.savefig(re.sub(".py", "", os.path.basename(__file__))+"_union.png")

if __name__ == "__main__":
    main()
