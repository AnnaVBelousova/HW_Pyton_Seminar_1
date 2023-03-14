# Задание 3.

# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.

# Пример:
# Введите число n: 3
# n + nn + nnn = 369

print("Введите число n:")
n = int(input())
num2 = n*10 + n
print(num2)
num3 = n*100+n*10+n
result = n + num2 + num3
print(result)