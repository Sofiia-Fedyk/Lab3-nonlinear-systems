"""
Графічна локалізація кореня і контроль через scipy.Вільгельм.
"""
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from scipy.optimize import fsolve

from common import X0, G, F

DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "localization.png")


def plot_localization(path=DEFAULT_PATH):
    t = np.linspace(-2.5, 2.5, 500)
    X, Y = np.meshgrid(t, t)
    Z = F(X, Y)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.contour(X, Y, Z[0], levels=[0], colors="tab:blue")
    ax.contour(X, Y, Z[1], levels=[0], colors="tab:red")

    (x_lo, x_hi), (y_lo, y_hi) = G["x"], G["y"]
    ax.add_patch(Rectangle((x_lo, y_lo), x_hi - x_lo, y_hi - y_lo,
                           fill=False, linestyle="--", edgecolor="black", linewidth=1.5))

    ax.legend(handles=[
        Line2D([0], [0], color="tab:blue", label="sin(x + y) + y = 2,6x"),
        Line2D([0], [0], color="tab:red", label="x² + y² = 4"),
        Line2D([0], [0], color="black", linestyle="--", label="область G"),
    ], loc="upper right")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.grid(True)

    plt.savefig(path)
    plt.close()


def fsolve_check():
    x, y = fsolve(lambda v: F(*v), X0)
    return float(x), float(y)


if __name__ == "__main__":
    plot_localization()
    print(fsolve_check())
