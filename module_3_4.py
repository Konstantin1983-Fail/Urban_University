def single_root_words(root_word, *other_words):
    # Преобразуем root_word в нижний регистр и сохраняем в отдельную переменную
    root_word_lower = root_word.lower()

    # Создаем пустой список
    same_words = []

    # Перебираем слова в *other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру для сравнения
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем образованный список
    return same_words


# Вызов функции с примерами и вывод результата
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Должен вывести: ['richiest', 'orichalcum', 'richies']
print(result2)  # Должен вывести: ['Able', 'Disable']
