def all_variants(text):
    # Цикл по длинам подпоследовательностей от 1 до длины строки
    for length in range(1, len(text) + 1):
        # Цикл по начальной позиции для подпоследовательности заданной длины
        for start in range(len(text) - length + 1):
            yield text[start:start + length]

# Пример использования:
a = all_variants("abc")

# Итерация по генератору
for i in a:
    print(i)
