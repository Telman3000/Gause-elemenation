# Nuruzov Telman DSAI-03

from sympy import Matrix


def compute_subspaces(matrix: Matrix):
    """
    Возвращает базисы трёх пространств:
      - Нуль-пространства A
      - Левого нуль-пространства A
      - Строкового пространства A
    """
    null_sp = matrix.nullspace()
    left_null_sp = matrix.T.nullspace()
    row_sp = matrix.rowspace()
    return null_sp, left_null_sp, row_sp


def format_and_print(space_name: str, vectors):
    print(f"{space_name}:")
    if not vectors:
        print("  └ empty basis ─ None")
    else:
        for vec in vectors:
            print(f"  └ {vec}")
    print()


def main():
    # Пример матрицы A
    A = Matrix([
        [1, 2, 1],
        [2, 4, 3],
        [3, 6, 4]
    ])

    ns, lns, rs = compute_subspaces(A)
    format_and_print("Null space basis", ns)
    format_and_print("Left null space basis", lns)
    format_and_print("Row space basis", rs)


if __name__ == "__main__":
    main()
