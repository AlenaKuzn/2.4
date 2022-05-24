#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 3

import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    A = list(map(int, input().split()))
    # Если список пуст, завершить программу.
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Найдем минимальный элемент
    minimum = min(A)

    # Проверяем элементы списка
    for x in range(len(A)):
        # Меняем местами минимальный и последний элемент
        if A[x] == minimum:
            A[-1], A[x] = A[x], A[-1]
    print("Преобразованный список:", A)
