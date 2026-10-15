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
    # Створюємо сітку 200x200 точок в області G
    x_vals = np.linspace(G['x'][0], G['x'][1], 200)
    y_vals = np.linspace(G['y'][0], G['y'][1], 200)
    X, Y = np.meshgrid(x_vals, y_vals)

    dphi1_dx = np.abs(np.cos(X + Y) / 2.6)
    dphi1_dy = np.abs((np.cos(X + Y) + 1.0) / 2.6)

    dphi2_dx = np.abs(X / np.sqrt(4.0 - X**2))
    dphi2_dy = np.zeros_like(X)


    q_row1 = np.max(dphi1_dx + dphi1_dy)
    q_row2 = np.max(dphi2_dx + dphi2_dy)
    q_row = max(q_row1, q_row2)

    q_col1 = np.max(dphi1_dx + dphi2_dx)
    q_col2 = np.max(dphi1_dy + dphi2_dy)
    q_col = max(q_col1, q_col2)

    valid_q = [q for q in (q_row, q_col) if q < 1.0]

    if not valid_q:
        raise ValueError("Жодна з норм не менша за 1!")

    return min(valid_q)


def stop_threshold(q, eps=EPS):
    """Поріг умови зупинки для МПІ і Зейделя. Готова, не змінювати."""
    return eps if q <= 0.5 else (1 - q) / q * eps


if __name__ == "__main__":
    q = estimate_q()
    print("q =", q, " поріг =", stop_threshold(q))
