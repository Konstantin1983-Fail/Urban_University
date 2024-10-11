from datetime import datetime
from multiprocessing import Pool


# Функция для считывания данных из файла
def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r') as file:  # Открываем файл для чтения
        while True:
            line = file.readline()  # Считываем строку
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line)  # Добавляем строку в список
    return all_data  # Возвращаем список данных (необязательно, просто для демонстрации)


# Список названий файлов
filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]  # Пример файлов file 1.txt, file 2.txt и т.д.

if __name__ == '__main__':
    # Линейный подход
    start = datetime.now()  # Начало измерения времени
    for filename in filenames:
        read_info(filename)  # Считываем файлы по очереди
    end = datetime.now()   # Конец измерения времени
    print(f" {end - start} Линейный")

    # Многопроцессный подход
    start = datetime.now()  # Начало измерения времени
    with Pool() as pool:  # Используем пул процессов
        pool.map(read_info, filenames)  # Параллельный вызов функции для каждого файла
    end = datetime.now()   # Конец измерения времени
    print(f" {end - start} Многопроцессный")
