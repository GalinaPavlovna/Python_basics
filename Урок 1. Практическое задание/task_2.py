"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
sec = input('Введите время в секундах:\n')
while not sec.isdigit():
    sec = input('У вас не вышло. Введите время в секундах:\n')
sec = int(sec)
print(f'Время в формате ч:м:с - {sec // 3600:02}:{sec // 60 - sec // 3600 * 60:02}:{sec % 60:02}')

# Извините, мне сильно глаза режет нецелое количество часов. Можно я так?
