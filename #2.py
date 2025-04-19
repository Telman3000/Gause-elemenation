import sys

# Status codes
OK = 0
ERR_NOT_SQUARE = 1
ERR_SINGULAR = 2


def is_square(matrix: list[list[float]]) -> bool:
    """Проверяет, является ли матрица квадратной."""
    size = len(matrix)
    return all(len(row) == size for row in matrix)


def augment_with_identity(matrix: list[list[float]]) -> list[list[float]]:
    """Создает расширенную матрицу [A | I] для Гаусс-Жордана."""
    size = len(matrix)
    return [row[:] + [1.0 if i == j else 0.0 for j in range(size)]
            for i, row in enumerate(matrix)]


def gauss_jordan_eliminate(aug: list[list[float]], eps: float = 1e-12) -> bool:
    """Применяет метод Гаусс-Жордана к расширенной матрице.
    Возвращает False, если матрица вырождена (нет обратной)."""
    size = len(aug)
    for k in range(size):
        # Нахождение строки с максимальным опорным элементом
        pivot_row = max(range(k, size), key=lambda r: abs(aug[r][k]))
        aug[k], aug[pivot_row] = aug[pivot_row], aug[k]

        pivot_val = aug[k][k]
        if abs(pivot_val) < eps:
            return False

        # Нормирование строки
        aug[k] = [val / pivot_val for val in aug[k]]

        # Обнуление остальных элементов столбца
        for i in range(size):
            if i != k:
                factor = aug[i][k]
                aug[i] = [curr - factor * piv for curr, piv in zip(aug[i], aug[k])]
    return True


def inverse_matrix(matrix: list[list[float]]) -> list:
    """
    Возвращает [status_code, inverse_or_error].
    status_code:
      0 (OK),
      1 (не квадратная),
      2 (вырожденная).
    """
    if not is_square(matrix):
        return [ERR_NOT_SQUARE, "The matrix must be squared"]

    # Копируем данные и создаем [A | I]
    source = [list(map(float, row)) for row in matrix]
    augmented = augment_with_identity(source)

    # Вычисляем с помощью Гаусс-Жордана
    if not gauss_jordan_eliminate(augmented):
        return [ERR_SINGULAR, "The matrix is singular, no inverse exists."]

    # Извлечение обратной матрицы из правой части
    n = len(augmented)
    inverse = [row[n:] for row in augmented]
    return [OK, inverse]


def read_matrix(n: int) -> list[list[float]]:
    """Считывает n строк матрицы с пользовательского ввода."""
    matrix = []
    for _ in range(n):
        matrix.append(list(map(float, input().split())))
    return matrix


def main():
    try:
        n = int(input("Enter the size of the square matrix (n x n): "))
        if n <= 0:
            print("Error(The matrix size must be a positive number)")
            return
    except ValueError:
        print("Error: Please enter valid numbers")
        return

    print("Enter the elements of the matrix row by row separated by spaces!!!:")
    matrix = read_matrix(n)
    if any(len(row) != n for row in matrix):
        print(f"Error(Please enter exactly {n} numbers in each row)")
        return

    status, result = inverse_matrix(matrix)
    if status == OK:
        print("\nInverse matrix:")
        for row in result:
            print(" ".join(f"{val:.6f}" for val in row))
    else:
        print(f"Error({result})")


if __name__ == "__main__":
    main()