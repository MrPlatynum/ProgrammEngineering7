#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(10)]

    # Вычисляем сумму положительных элементов с использованием List Comprehensions
    positive_sum = sum(num for num in A if num > 0)

    print(f"Сумма положительных элементов: {positive_sum}")



