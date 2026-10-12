"""
Метод Зейделя.Діана.
"""
from common import EPS, X0, MAX_ITER, phi1, phi2, make_result
from convergence import estimate_q, stop_threshold


def seidel(x0=X0, eps=EPS, q=None):
    """
    Повертає make_result("Зейдель", history).
    Нічого не друкує і не малює.
    """
    if q is None:
        q = estimate_q()
    x, y = x0
    history = [(0, x, y, None, None, None)]

    for k in range(1, MAX_ITER + 1):
        raise NotImplementedError

    raise RuntimeError("Метод Зейделя не зійшовся")


if __name__ == "__main__":
    r = seidel()
    print(r["x"], r["y"], r["iters"])
