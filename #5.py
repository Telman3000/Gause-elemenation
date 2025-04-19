# Nuruzov Telman DSAI-03

import numpy as np

# Настройки вывода numpy-массивов
np.set_printoptions(suppress=True, precision=2, floatmode='fixed')

def orthonormalize(vectors: list[list[float]]) -> np.ndarray:
    """
    Приводит список векторов к базису методом Грама-Шмидта (не фильтруя почти нулевые).

    Args:
        vectors: список векторов (каждый как список чисел).

    Returns:
        Массив shape (k, n), где k равно числу исходных векторов.
    """
    basis = []
    for vec in vectors:
        v = np.array(vec, dtype=float)
        for u in basis:
            v -= np.dot(u, v) * u
        norm = np.linalg.norm(v)
        # включаем любой ненулевой результат (как в оригинале)
        if norm != 0:
            basis.append(v / norm)
    return np.array(basis)


def read_vectors(count: int) -> list[list[float]]:
    """Считывает count векторов от пользователя."""
    pts = []
    for i in range(1, count + 1):
        vals = list(map(float, input(f"Vector #{i} (space-separated): ").split()))
        pts.append(vals)
    return pts


def main():
    try:
        n = int(input("How many vectors? "))
        if n < 1:
            raise ValueError
    except ValueError:
        print("Please enter a positive integer.")
        return

    vectors = read_vectors(n)
    ortho = orthonormalize(vectors)

    print("\nOrthonormal basis:")
    print(ortho)


if __name__ == "__main__":
    main()
