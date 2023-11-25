#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = []
    for i in range(10):
        elem = int(input(f"Введите элемент {i + 1}: "))
        A.append(elem)

    positive_sum = 0

    for num in A:
        if num > 0:
            positive_sum += num

    print(f"Сумма положительных элементов: {positive_sum}")
