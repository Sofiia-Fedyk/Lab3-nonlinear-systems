"""
Графічна локалізація кореня і контроль через scipy.Вільгельм.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

from common import F, G, X0

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
