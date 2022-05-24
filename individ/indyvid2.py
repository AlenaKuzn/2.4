#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 3

if __name__ == '__main__':
    a = list(map(int, input().split()))
    c, k = 0, 0
    m = 1

    # Произведение элементов с четными номерами
    for i in a:
        if i % 2 == 0:
            m *= a[i]

    # Находим сумму между нулями
    for i in a:
        if i == 0:
            if k == 1:
                break
            k = 1
            continue
        if k == 1:
            c += i

    print("Произведение элементов с четными номерами: ", m)
    print("Сумма между нулями", c)
    print("Преобразованный список", a)
