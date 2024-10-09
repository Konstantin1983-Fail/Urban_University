from time import sleep, time  # Импортируем функции sleep и time из модуля time
from threading import Thread  # Импортируем класс Thread из модуля threading

def write_words(word_count, file_name):
    # Функция для записи word_count слов в указанный файл file_name
    with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл в режиме записи с кодировкой utf-8
        for i in range(1, word_count + 1):  # Цикл от 1 до word_count
            file.write(f"Какое-то слово N° {i}\n")  # Записываем слово в файл с нужным форматом
            sleep(0.1)  # Пауза 0.1 секунды после записи
    print(f"Завершилась запись в файл {file_name}")  # Выводим сообщение о завершении записи

# Измеряем время выполнения вызовов функции write_words
start_time = time()  # Запоминаем текущее время
write_words(10, 'example1.txt')  # Вызов функции для записи 10 слов в example1.txt
write_words(30, 'example2.txt')  # Вызов функции для записи 30 слов в example2.txt
write_words(200, 'example3.txt')  # Вызов функции для записи 200 слов в example3.txt
write_words(100, 'example4.txt')  # Вызов функции для записи 100 слов в example4.txt
end_time = time()  # Запоминаем время окончания
print(f"Работа функций {end_time - start_time:.6f} секунд")  # Выводим время выполнения функций

# Измеряем время выполнения потоков
def thread_function(word_count, file_name):
    # Функция для вызова write_words из потоков
    write_words(word_count, file_name)

start_time_threads = time()  # Запоминаем текущее время для потоков

# Создаем и запускаем потоки для записи в файлы
threads = [
    Thread(target=thread_function, args=(10, 'example5.txt')),  # Поток для записи 10 слов
    Thread(target=thread_function, args=(30, 'example6.txt')),  # Поток для записи 30 слов
    Thread(target=thread_function, args=(200, 'example7.txt')),  # Поток для записи 200 слов
    Thread(target=thread_function, args=(100, 'example8.txt'))   # Поток для записи 100 слов
]

# Запускаем потоки
for thread in threads:
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

end_time_threads = time()  # Запоминаем время окончания потоков
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")  # Выводим время выполнения потоков

# Код написан в 2024 году
