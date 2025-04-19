# Nuruzov Telman DSAI-03

import sys
from typing import List, Tuple


def rref(matrix: List[List[float]], tol: float = 1e-12) -> Tuple[List[List[float]], List[int]]:
    """
    Приводит матрицу к сокращенной ступенчатой форме и возвращает рредукцию и список индексов ведущих столбцов.
    """
    M = [row[:] for row in matrix]
    rows, cols = len(M), len(M[0])
    pivot_cols = []
    r = 0
    for c in range(cols):
        # найти опорный элемент
        pivot = max(range(r, rows), key=lambda i: abs(M[i][c])) if r < rows else None
        if r < rows and abs(M[pivot][c]) > tol:
            M[r], M[pivot] = M[pivot], M[r]
            # нормализация
            fac = M[r][c]
            M[r] = [val / fac for val in M[r]]
            # исключение
            for i in range(rows):
                if i != r:
                    fac2 = M[i][c]
                    M[i] = [iv - fac2 * rv for iv, rv in zip(M[i], M[r])]
            pivot_cols.append(c)
            r += 1
        if r == rows:
            break
    return M, pivot_cols


def column_space(matrix: List[List[float]]) -> List[List[float]]:
    """Возвращает базис столбцового пространства (колонки оригинальной матрицы)."""
    _, pivots = rref(matrix)
    # каждая ведущая колонка является базисом
    return [[row[c] for row in matrix] for c in pivots]


def row_space(matrix: List[List[float]]) -> List[List[float]]:
    """Возвращает базис строкового пространства (строки матрицы в rref)."""
    R, pivots = rref(matrix)
    # строки до количества ведущих
    rank = len(pivots)
    return [R[i] for i in range(rank)]


def null_space(matrix: List[List[float]]) -> List[List[float]]:
    """Возвращает базис пространства решений Ax = 0 (нуль-пространство столбцов)."""
    R, pivots = rref(matrix)
    rows, cols = len(R), len(R[0])
    free_vars = [c for c in range(cols) if c not in pivots]
    basis = []
    for fv in free_vars:
        vec = [0.0] * cols
        vec[fv] = 1.0
        for i, pc in enumerate(pivots):
            vec[pc] = -R[i][fv]
        basis.append(vec)
    return basis


def left_null_space(matrix: List[List[float]]) -> List[List[float]]:
    """Возвращает базис левого нуль-пространства (строки x такие, что xA=0)."""
    # левое нуль-пространство = ноль-пространство транспонированной матрицы
    MT = list(map(list, zip(*matrix)))
    return null_space(MT)


def print_space(name: str, space: List[List[float]]):
    print(f"\n{name} (dimension={len(space)}):")
    if not space:
        print("  {{0}}")
    for v in space:
        print("  [" + ", ".join(f"{x:.4f}" for x in v) + "]")


def main():
    try:
        m = int(input("Number of rows: "))
        n = int(input("Number of cols: "))
    except ValueError:
        print("Invalid dimensions.")
        sys.exit(1)
    print("Enter matrix row by row (entries separated by spaces):")
    A = []
    for _ in range(m):
        row = list(map(float, input().split()))
        if len(row) != n:
            print(f"Each row must have {n} entries.")
            sys.exit(1)
        A.append(row)

    print_space("Column Space", column_space(A))
    print_space("Row Space", row_space(A))
    print_space("Null Space", null_space(A))
    print_space("Left Null Space", left_null_space(A))


if __name__ == "__main__":
    main()
