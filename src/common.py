"""
Спільні дані для всієї команди. Автор: Софія.
Інші учасники лише ІМПОРТУЮТЬ звідси, нічого не змінюють.

Варіант 3:
    sin(x + y) + y = 2,6x
    x^2 + y^2 = 4            (x < 0, y < 0)
"""
import numpy as np

EPS = 1e-3                              # точність
X0 = (-0.9, -1.8)                       # початкове наближення
G = {"x": (-1.0, -0.7), "y": (-1.9, -1.7)}  # область ізоляції кореня
MAX_ITER = 100                          # захист від нескінченного циклу


#Система у вигляді F(x, y) = 0
def F(x, y):
    """Вектор [f1, f2]."""
    return np.array([np.sin(x + y) + y - 2.6 * x,
                     x ** 2 + y ** 2 - 4])


def W(x, y):
    """Матриця Якобі системи F (для методу Ньютона)."""
    c = np.cos(x + y)
    return np.array([[c - 2.6, c + 1],
                     [2 * x,   2 * y]])


#Ітераційний вигляд x = phi(x) (для МПІ і Зейделя)
def phi1(x, y):
    return (np.sin(x + y) + y) / 2.6


def phi2(x, y):
    return -np.sqrt(4 - x ** 2)


#Єдиний формат результату
HISTORY_COLUMNS = ["k", "x", "y", "|Δx|", "|Δy|", "Δ"]


def make_result(method, history):
    """
    method  - назва методу (рядок)
    history - список кортежів (k, x, y, dx, dy, delta);
              перший рядок: (0, x0, y0, None, None, None)
    """
    k, x, y, *_ = history[-1]
    return {"method": method, "x": float(x), "y": float(y),
            "iters": k, "history": history}
