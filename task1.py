# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.
#
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
#
# Вывод: Парам пам-пам

song = 'пара-ра-ром рам-пам-папам пе-ра-пе-да' #input('введите текст песни')
answer_yes = 'Парам пам-пам'
answer_no = 'Пам парам'
vovels = 'аоуеяию'
song2 = song.split()
result = []
print(f'ПЕСНЯ: {song}')
for i in song2:
    count = 0
    for letter in i:
        if letter in vovels:
            count += 1
    result.append(count)
result_new = list(set(result))
if len(result_new) < 2:
    print(f'Ответ: {answer_yes}')
else:
    print(f'Ответ: {answer_no}')
