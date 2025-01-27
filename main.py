def gauss_elimination(matrix, rhs):
    n = 3
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        rhs[i], rhs[max_row] = rhs[max_row], rhs[i]
        lead = matrix[i][i]
        if lead == 0:
            raise ValueError("Ошибка")
        matrix[i] = [m / lead for m in matrix[i]]
        rhs[i] /= lead
        for j in range(i + 1, n):
            factor = matrix[j][i]
            matrix[j] = [mj - factor * mi for mj, mi in zip(matrix[j], matrix[i])]
            rhs[j] -= factor * rhs[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = rhs[i] - sum(matrix[i][j] * x[j] for j in range(i + 1, n))
    return x

# Ввод матрицы A и вектора b через консоль
n = 3
A = []
b = []

print("Введите элементы матрицы A (3x3) построчно, разделяя пробелами:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)
    print("Ведите следующий ряд:")
    

print("Введите элементы вектора b (3), разделяя пробелами:")
b = list(map(float, input().split()))

# Вычисление решения и вывод
solution = gauss_elimination(A, b)
print("Решение:", solution)