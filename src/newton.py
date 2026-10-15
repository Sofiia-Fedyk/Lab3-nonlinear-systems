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
        f1, f2 = F(x, y)
        (a, b), (c, d) = W(x, y)

        # W·[dx, dy] = -F, розв'язок за Крамером
        det = a * d - b * c
        if det == 0:
            raise RuntimeError("Матриця Якобі вироджена, метод Ньютона не може продовжити")
        dx = (-f1 * d - b * (-f2)) / det
        dy = (a * (-f2) - (-f1) * c) / det

        x += dx
        y += dy
        delta = max(abs(dx), abs(dy))
        history.append((k, float(x), float(y), float(abs(dx)), float(abs(dy)), float(delta)))

        if delta <= eps:
            return make_result("Ньютон", history)

    raise RuntimeError(f"Метод Ньютона не зійшовся за {MAX_ITER} ітерацій")


if __name__ == "__main__":
    res = newton()
    print(res["method"], res["x"], res["y"], res["iters"])
    for row in res["history"]:
        print(row)
