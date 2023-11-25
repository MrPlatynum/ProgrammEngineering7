#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    numbers = list(map(int, input("Enter a list of integer elements separated by space: ").split()))

    max_index = numbers.index(max(numbers))

    # 2. Find the product of elements between the first and second zero elements.
    if 0 in numbers:
        first_zero_index = numbers.index(0)
    else:
        first_zero_index = -1
    if first_zero_index != -1:
        second_zero_index = numbers.index(0, first_zero_index + 1)
    else:
        second_zero_index = -1
    product_between_zeros = 1

    if first_zero_index != -1 and second_zero_index != -1:
        for num in numbers[first_zero_index + 1:second_zero_index]:
            product_between_zeros *= num

    # Transform the list.
    transformed_list = numbers[1::2] + numbers[0::2]

    print("Index of the maximum element:", max_index)
    print("Product of elements between the first and second zero elements:", product_between_zeros)
    print("Transformed list:", transformed_list)
