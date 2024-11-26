import numpy as np
import matplotlib.pyplot as plt


def bjerum_diagram(ph, pKa):
    # Bruger den omksrevet pufferligning ph = pKa + log([A-]/[HA])
    # Omksrives til ph = pKa + log((1-ys)/(ys)) ved brug a syre brøken ys = [HA]/([HA]+[A-])
    # x = (1-ys)/ys -> ys = 1/(1+x)
    ys_ratio = 10 ** (ph - pKa)
    acid_ratio = 1 / (1 + ys_ratio)
    return acid_ratio


def plot_bjerum_diagram(pka, ax=None):
    ph = np.linspace(0, 14, 100)
    all_ratio = []
    if isinstance(pka, (int, float)):
        pka = [pka]
    if ax is None:
        fig, ax = plt.subplots()
    for p in pka:
        ax.plot(ph, ratio := bjerum_diagram(ph, p), label=f"pKa = {p}")
        all_ratio.append(ratio)
    ax.legend()
    ax.set_xlabel("pH")
    ax.set_ylabel("HA/A-")

    return np.vstack(all_ratio)


def plot_2D_bjerum_diagram(grid_size, min_pka, max_pka):
    ph = np.linspace(0, 14, grid_size)
    pka = np.linspace(min_pka, max_pka, grid_size)
    xx, yy = np.meshgrid(ph, pka)
    zz = bjerum_diagram(xx, yy)
    fig, ax = plt.subplots()
    cntr = ax.contourf(xx, yy, zz, levels=10, cmap="inferno", vmin=0, vmax=1)
    ax.set_xlabel("pH")
    ax.set_ylabel("pKa")
    clb = plt.colorbar(cntr, ax=ax)
    ax.grid()
    ax.set_title("Bjerum Diagram")
    return ax
