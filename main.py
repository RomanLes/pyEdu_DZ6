# Узнать куда показывает минутная стрелка
a = 38746298762973632324233242  # Подсчитанное количество минут
b = 60  # 1 час == 60 минут
print(a, '%', b, '=', a % b)  # Остаток от деления
print('Минутная стрелка показывает на:', a % b, 'минуты')
