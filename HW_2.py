# Задание 2.

# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600

seconds = int(input())

minutes = seconds//60
print(minutes)
hours = seconds//3600
round(minutes, 1)
round(hours, 1)


time = f'{hours} : {minutes} : {seconds}'
print(time)

