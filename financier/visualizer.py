#!/usr/bin/env python3

def plot_income(df, fname=None):
    """Plot an offer df, if fname is None save to a file named fname"""
    import matplotlib
    from matplotlib import pyplot as plt
    ax = df.plot(kind="bar", figsize=(20, 6), fontsize=15)
    ax.set_yticks((range(0, int(df.max()[0]), 50000)), minor=True)
    ax.grid(True, which='minor', axis='y')
    ax.set_ylabel("$ Amount")
    plt.tight_layout()
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    if fname is None:
        plt.show()
    else:
        plt.savefig(fname)
