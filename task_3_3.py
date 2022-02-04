"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def substring(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            h = hashlib.md5(a[i:j].encode('utf-8')).hexdigest()
            if not hash_word.get(h) and a != a[i:j]:
                hash_word[h] = a[i:j]
    return len(hash_word)


hash_word = {}
word = 'papa'
print(f'{word} - {substring(word)} уникальных подстрок')
for key, val in hash_word.items():
    print(val)
