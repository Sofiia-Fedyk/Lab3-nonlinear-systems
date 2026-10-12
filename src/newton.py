"""
Метод Ньютона.Вільгельм.
"""
from common import EPS, X0, MAX_ITER, F, W, make_result


def newton(x0=X0, eps=EPS):
    """
    Повертає make_result("Ньютон", history).
    Нічого не друкує і не малює.
    """
    x, y = x0
    history = [(0, x, y, None, None, None)]

    for k in range(1, MAX_ITER + 1):
        raise NotImplementedError

    raise RuntimeError("Метод Ньютона не зійшовся")


if __name__ == "__main__":
    r = newton()
    print(r["x"], r["y"], r["iters"])
