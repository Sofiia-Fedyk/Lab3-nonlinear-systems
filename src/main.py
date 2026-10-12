"""
Точка входу: запускає всі методи, друкує таблиці, зберігає результати.
Софія.
"""
import os
import pandas as pd

from common import EPS, X0, G, F, HISTORY_COLUMNS
from newton import newton
from simple_iteration import simple_iteration
from seidel import seidel
from convergence import estimate_q, stop_threshold
from localization import plot_localization, fsolve_check

RESULTS_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAMES = {"Ньютон": "newton", "МПІ": "simple_iteration", "Зейдель": "seidel"}


def history_table(result):
    """DataFrame з history методу, округлений до 5 знаків."""
    raise NotImplementedError


def main(): 
    raise NotImplementedError


if __name__ == "__main__":
    main()
