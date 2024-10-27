import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов в атрибуте file_names
        self.file_names = file_names

    def get_all_words(self):
        # Подготовка пустого словаря для записи всех слов
        all_words = {}
        # Перебор всех файлов
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Чтение файла, перевод в нижний регистр
                text = file.read().lower()
                # Убираем пунктуацию
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')
                # Разбиваем строку на слова
                words = text.split()
                # Добавляем в словарь: ключ - имя файла, значение - список слов
                all_words[file_name] = words
        return all_words

    def find(self, word):
        # Используем метод get_all_words для получения всех слов
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()
        result = {}
        # Поиск первого вхождения слова
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # Позиция первого слова
            else:
                result[name] = None  # Если слова нет
        return result

    def count(self, word):
        # Используем метод get_all_words для получения всех слов
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()
        result = {}
        # Подсчёт количества вхождений слова
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


# Пример использования
finder = WordsFinder('test_file.txt')

# Получаем все слова из файлов
print(finder.get_all_words())

# Ищем слово "text"
print(finder.find('TEXT'))

# Считаем количество вхождений слова "teXT"
print(finder.count('teXT'))
