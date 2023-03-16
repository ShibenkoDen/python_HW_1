"""
Задача 2: Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""

number = int(input("Введите трехзначное число: "))
first_digit = number % 10
number = number / 10
second_digit = number % 10
third_number = number / 10

sum_of_digits = first_digit+second_digit+third_number
print(int(sum_of_digits))
