import numpy as np


def proverka(a, n):
    for i in range(n):
        diag = np.abs(a[i, i])
        diag_sum = np.sum(np.abs(a[i, :])) - diag
        if diag <= diag_sum:
            return False
        return True


def jacobi_method(a, b):
    n = len(b)
    tochnost = 0.001
    x = np.zeros(n, dtype="float32")
    x_new = np.zeros(n, dtype="float32")
    # Проверка сходимости
    if proverka(a, n):
        while True:
            for i in range(n):
                x_new[i] = (b[i] - ((np.dot(a[i, :], x)) - a[i, i] * x[i])) / a[i, i]
            diff = np.abs(x_new - x)
            if np.all(diff < 0.001):
                return x_new
            x = np.copy(x_new)


# Главная программа
n_unknowns = int(input('Введите число неизвестных: '))

print('Введите коэффициенты при неизвестных:')
a = np.zeros((n_unknowns, n_unknowns), dtype="float32")
for i in range(n_unknowns):
    for j in range(n_unknowns):
        a[i, j] = float(input())

print('Введите свободные коэффициенты:')
b = np.zeros(n_unknowns, dtype="float32")
for i in range(n_unknowns):
    b[i] = float(input())

print('Значения коэффициентов:')
for i in range(n_unknowns):
    for j in range(n_unknowns):
        print('{0:+.3f}'.format(a[i, j]), end=' ')
    print(' | {0:+.3f}'.format(b[i]), end='\n')

print('Значения неизвестных:')
x = jacobi_method(a, b)
for i in range(n_unknowns):
    print('{0:+.3f}'.format(x[i]), end=' ')

print()
