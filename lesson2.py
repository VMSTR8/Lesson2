# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
i = 'ауоыиэяюёе'
count = 0
for x in word.lower():
    for x2 in i:
        if x2 in x:
            count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for x in sentence.split():
    print(x[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
average = sum(len(word) for word in words) / len(words)
print(average)
print(sum(len(word) for word in sentence.split()) / len(sentence.split()))
