# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод:
# Парам пам-пам
def counter_vowels(verse):
    vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
    vowels_amount = []
    vowels_amount = list(map(lambda phrases: sum([len(list(filter(lambda symbol: symbol in vowels, word)))
    for word in phrases.split('-')]), verse.split()))
    return all(x == vowels_amount[0] for x in vowels_amount)
verse = input('Введите стих: \n')
print("Парам пам-пам" if counter_vowels(verse) else "Пам парам")