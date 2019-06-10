import json
import re
import os
import glob
from matplotlib import pyplot as plt
import numpy as np


def read_json(file_name):
    f = open(file_name, "r")
    json_dict = json.load(f)
    return json_dict['SNR'], json_dict['BER']


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    fn_list = glob.glob("./*.json")
    label_list = [(fn.split("/")[-1]).split(".")[0] for fn in fn_list]

    for i, (fn, label) in enumerate(zip(fn_list, label_list)):
        snr, ber = read_json(fn)
        ax.plot(snr, ber, label=label, color="C"+str(i))

        ax.plot(snr, np.poly1d(np.polyfit(snr, ber, 8))(snr),
                label=label+"(polyfit)", color="C"+str(i), linestyle=":")

    ax.set_yscale("log")
    ax.set_xlim([0, 30])
    ax.set_ylim([1e-5, 1])

    ax.set_xlabel("SNR")
    ax.set_ylabel("BER")

    ax.legend()
    ax.grid()

    plt.savefig(re.sub(".py", "", os.path.basename(__file__))+".svg",
                format="svg")
    # plt.savefig(re.sub(".py", "", os.path.basename(__file__))+".png")


if __name__ == '__main__':
    main()
