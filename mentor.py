#______________________________________________________Задача №1________________________________________________________

def find_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    with open("area.txt", 'w', encoding='UTF-8') as file:
        file.write(f'Площадь треугольника = {area}')

    side_1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    side_2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    side_3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

    if side_1 ** 2 + side_2 ** 2 == side_3 ** 2:
        with open('truefalse.txt', 'w', encoding='UTF-8') as file:
            file.write('True')
    else:
        with open('truefalse.txt', 'w', encoding='UTF-8') as file:
            file.write('False')

find_area(1, 2, 2, 5, 1, 7)

#______________________________________________________Задача №2________________________________________________________

from collections import Counter

def find_most_common_word(sentence):
    words = sentence.split()
    word_counts = Counter()

    for word in words:
        if word.isalpha():
            word_counts[word] += 1
        else:
            continue

    most_common_word = max(word_counts, key=lambda x: word_counts[x])
    return most_common_word

user_sentence = input("Введите предложение: ")
most_common = find_most_common_word(user_sentence)
print("Самое часто встречающееся слово:", most_common)

#______________________________________________________Задача №3________________________________________________________

from datetime import time

n = int(input("Введите количество временных отрезков(двухзначные числа): "))

time_list = [time(*map(int, input("Введите времена поочередно через пробел: ").split())) for i in range(n)]
time_list.sort()

for time in time_list:
    print(*time_list)
