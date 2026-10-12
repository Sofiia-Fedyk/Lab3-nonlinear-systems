"""
Спільні дані для всієї команди. Автор: Софія.
Інші учасники лише ІМПОРТУЮТЬ звідси, нічого не змінюють.

Варіант 3:
    sin(x + y) + y = 2,6x
    x^2 + y^2 = 4            (x < 0, y < 0)
"""
import numpy as np

EPS = None        
X0 = None         
G = None          
MAX_ITER = None   


#Система у вигляді F(x, y) = 0
def F(x, y):
    """Вектор [f1, f2]."""
    raise NotImplementedError


def W(x, y):
    """Матриця Якобі системи F (для методу Ньютона)."""
    raise NotImplementedError


#Ітераційний вигляд x = phi(x) (для МПІ і Зейделя)
def phi1(x, y):
    raise NotImplementedError


def phi2(x, y):
    raise NotImplementedError


#Єдиний формат результату
HISTORY_COLUMNS = ["k", "x", "y", "|Δx|", "|Δy|", "Δ"]


def make_result(method, history):
    """
    method  - назва методу (рядок)
    history - список кортежів (k, x, y, dx, dy, delta);
              перший рядок: (0, x0, y0, None, None, None)
    Повертає {"method", "x", "y", "iters", "history"}.
    """
    raise NotImplementedError
