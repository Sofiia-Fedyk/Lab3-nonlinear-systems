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

RESULTS_DIR = os.path.dirname(os.path.abspath(__file__))  # папка src
FILE_NAMES = {"Ньютон": "newton", "МПІ": "simple_iteration", "Зейдель": "seidel"}


def history_table(result):
    df = pd.DataFrame(result["history"], columns=HISTORY_COLUMNS)
    return df.round(5)


def main():
    pd.set_option("display.width", 120)

    print("Лабораторна робота №3, варіант 3")
    print(f"G: x ∈ {G['x']}, y ∈ {G['y']};  x0 = {X0};  ε = {EPS}\n")

    plot_localization(os.path.join(RESULTS_DIR, "localization.png"))

    q = estimate_q()
    print(f"q = {q:.4f};  поріг зупинки МПІ/Зейделя = {stop_threshold(q):.6f}\n")

    results = [newton(), simple_iteration(q=q), seidel(q=q)]

    for r in results:
        table = history_table(r)
        print(f" {r['method']} ")
        print(table.to_string(index=False), "\n")
        table.to_csv(os.path.join(RESULTS_DIR, FILE_NAMES[r["method"]] + ".csv"),
                     index=False)

    summary = pd.DataFrame([{
        "Метод": r["method"],
        "x*": round(r["x"], 5),
        "y*": round(r["y"], 5),
        "Ітерацій": r["iters"],
        "|f1(x*)|": abs(F(r["x"], r["y"])[0]),
        "|f2(x*)|": abs(F(r["x"], r["y"])[1]),
    } for r in results])
    print(" Порівняння методів ")
    print(summary.to_string(index=False), "\n")
    summary.to_csv(os.path.join(RESULTS_DIR, "summary.csv"), index=False)

    xs, ys = fsolve_check()
    print(f"x = {xs:.5f}, y = {ys:.5f}")
    print(f"Відповідь: x* ≈ {results[0]['x']:.3f}, y* ≈ {results[0]['y']:.3f}")


if __name__ == "__main__":
    main()

