"""
Оцінка збіжності для МПІ і Зейделя.Діана.
"""
import numpy as np

from common import EPS, G


def estimate_q():
    """
    Числова оцінка q = max норми матриці Якобі для phi на сітці в G.
    Повертає q (float) за тією нормою (рядки або стовпці), де q < 1 і менше.
    """
    raise NotImplementedError


def stop_threshold(q, eps=EPS):
    """Поріг умови зупинки для МПІ і Зейделя. Готова, не змінювати."""
    return eps if q <= 0.5 else (1 - q) / q * eps


if __name__ == "__main__":
    q = estimate_q()
    print("q =", q, " поріг =", stop_threshold(q))
