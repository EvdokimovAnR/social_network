import random
import numpy as np

low_value = float(input('Введите левую границу диапазона коэффициентов: '))
high_value = float(input('Введите правую границу диапазона коэффициентов: '))
n_unknowns = int(input('Введите число неизвестных: '))

a = np.zeros((n_unknowns, n_unknowns), dtype="int64")
b = np.zeros(n_unknowns, dtype="int64")
x = np.zeros(n_unknowns, dtype="int64")

for i in range(n_unknowns):
    for j in range(n_unknowns):
        temp = 0
        while temp == 0:
            temp = random.randint(low_value, high_value)
        a[i, j] = temp

    sum = 0
    for j in range(n_unknowns):
        if j != i:
            sum = sum + abs(a[i, j])
    while abs(sum) >= abs(a[i, i]):
        if a[i, i] > 0:
            a[i, i] = a[i, i] + 1
        else:
            a[i, i] = a[i, i] - 1
        sum = 0
        for j in range(n_unknowns):
            if j != i:
                sum = sum + abs(a[i, j])
    temp = 0
    while temp == 0:
        temp = random.randint(low_value, high_value)
    x[i] = temp

for i in range(n_unknowns):
    b[i] = np.dot(a[i, :], x[:])
for i in range(n_unknowns):
    for j in range(n_unknowns):
        print('{0:+5n}'.format(a[i, j]), end=' ')
    print(' | {0:+5n}'.format(b[i]), end='\n')

for i in range(n_unknowns):
    print('{0:+5n}'.format(x[i]), end=' ')

print()