#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
my_favorite_movies_arr = []
n = 0
for i in range(len(my_favorite_movies)-1):
    if my_favorite_movies[i]+my_favorite_movies[i+1] == ', ':
        my_favorite_movies_arr.append(my_favorite_movies[n:i])
        n = i+2
    if i+1 == len(my_favorite_movies)-1:
        my_favorite_movies_arr.append(my_favorite_movies[n:i+2])
del(n)

print(my_favorite_movies_arr[0])
print(my_favorite_movies_arr[-1])
print(my_favorite_movies_arr[1])
print(my_favorite_movies_arr[-2])