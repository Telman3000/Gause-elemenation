#1 Gause elemenation

import sys

def input_system():
    try:
        n = int(input("Сколько уравнений в системе? "))
    except ValueError:
        print("Ошибка ввода числа уравнений.")
        sys.exit(1)
    print("Введите строки коэффициентов и свободных членов через пробел.")
    print("Пример для 2x + 3y - z = 7: 2 3 -1 7")
    system = []
    for i in range(1, n + 1):
        parts = input(f"Уравнение {i}: ").split()
        if len(parts) != n + 1:
            print(f"Ожидалось {n+1} чисел, получено {len(parts)}.")
            sys.exit(1)
        system.append([float(x) for x in parts])
    return system


def normalize_row(matrix, row_idx, pivot_col):
    pivot = matrix[row_idx][pivot_col]
    matrix[row_idx] = [val / pivot for val in matrix[row_idx]]


def eliminate(matrix, src_row, target_row, pivot_col):
    factor = matrix[target_row][pivot_col]
    matrix[target_row] = [tv - factor * sv for sv, tv in zip(matrix[src_row], matrix[target_row])]


def gaussian_eliminate(matrix):
    rows = len(matrix)
    for i in range(rows):
        # Выбор лучшего опорного элемента
        best = max(range(i, rows), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[best] = matrix[best], matrix[i]
        if abs(matrix[i][i]) < 1e-12:
            continue
        normalize_row(matrix, i, i)
        for r in range(rows):
            if r != i:
                eliminate(matrix, i, r, i)
    return matrix


def extract_solution(matrix):
    vars_count = len(matrix[0]) - 1
    solution = [None] * vars_count
    for row in matrix:
        coeffs, const = row[:-1], row[-1]
        if all(abs(c) < 1e-12 for c in coeffs):
            if abs(const) > 1e-12:
                return "Система несовместна"
            continue
        lead = next((i for i, c in enumerate(coeffs) if abs(c) > 1e-12), None)
        if lead is not None:
            solution[lead] = const
    if any(v is None for v in solution):
        free = [f"x{i+1}" for i, v in enumerate(solution) if v is None]
        return f"Бесконечно много решений. Свободные переменные: {', '.join(free)}"
    return "; ".join(f"x{i+1}={round(val,4)}" for i, val in enumerate(solution))


def main():
    matrix = input_system()
    print("\nИсходная расширенная матрица:")
    for row in matrix:
        print(row)
    reduced = gaussian_eliminate(matrix)
    print("\nПосле приведения:")
    for row in reduced:
        print(row)
    print("\nРешение:", extract_solution(reduced))

if __name__ == "__main__":
    main()

