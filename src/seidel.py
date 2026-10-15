"""
Реалізація методу Зейделя. Діана.
"""
from common import X0, EPS, MAX_ITER, phi1, phi2, make_result
from convergence import estimate_q, stop_threshold

def seidel(x0=X0, eps=EPS, q=None):
    if q is None:
        q = estimate_q()

    threshold = stop_threshold(q, eps)

    if isinstance(x0, dict):
        x, y = x0['x'], x0['y']
    else:
        x, y = x0[0], x0[1]

    history = [(0, x, y, None, None, None)]

    for k in range(1, MAX_ITER + 1):
        x_old = x
        y_old = y

        # КРОК ЗЕЙДЕЛЯ:
        x = phi1(x_old, y_old)
        y = phi2(x, y_old)

        dx = abs(x - x_old)
        dy = abs(y - y_old)
        delta = max(dx, dy)

        history.append((k, x, y, dx, dy, delta))

        if delta <= threshold:
            return make_result("Зейдель", history)

    raise RuntimeError(f"Метод не зійшовся за {MAX_ITER} кроків")


if __name__ == "__main__":
    res = seidel()
    print("Останній крок (повинно бути близько 5):", res['history'][-1][0])
    print("x =", res['history'][-1][1])
    print("y =", res['history'][-1][2])