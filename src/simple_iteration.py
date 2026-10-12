"""
Метод простої ітерації. Автор: Софія.
"""
from common import EPS, X0, MAX_ITER, phi1, phi2, make_result
from convergence import estimate_q, stop_threshold


def simple_iteration(x0=X0, eps=EPS, q=None):
    """
    Повертає make_result("МПІ", history).
    Нічого не друкує і не малює.
    """
    if q is None:
        q = estimate_q()
    x, y = x0
    history = [(0, x, y, None, None, None)]

    for k in range(1, MAX_ITER + 1):
        raise NotImplementedError

    raise RuntimeError("МПІ не зійшовся")


if __name__ == "__main__":
    r = simple_iteration()
    print(r["x"], r["y"], r["iters"])
