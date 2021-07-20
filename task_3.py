'''
Задание: Напишите функцию, которая будет принимать целое положительное число и определять, делится ли оно нацело на сумму цифр этого числа.

Примеры:

is_divisible(75) ➞ False
# 7 + 5 = 12
# 75 не делится нацело на 12

is_divisible(171) ➞ True
# 1 + 7 + 1 = 9
# 171 делится на 9 без остатка

is_divisible(481) ➞ True
is_divisible(89) ➞ False
is_divisible(516) ➞ True
is_divisible(200) ➞ True
'''

def is_divisible(num):
    return num % sum(map(int, str(num))) == 0