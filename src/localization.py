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

from common import F, G, X0
from common import X0, G, F

DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "localization.png")



SRC_DIR = os.path.dirname(os.path.abspath(__file__))


def plot_localization(path=os.path.join(SRC_DIR, "localization.png")):
    """
    Будує криві f1 = 0 і f2 = 0 та прямокутник G, зберігає у path.
    Нічого не повертає.
    """
    raise NotImplementedError


def fsolve_check():
    """Повертає (x, y), знайдені scipy.optimize.fsolve з X0."""
    raise NotImplementedError


if __name__ == "__main__":
    plot_localization()
    print(fsolve_check())
