# Функция для проверки, является ли число простым
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция-декоратор
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        if check_prime(result):  # Проверяем, является ли результат простым числом
            print("Простое")
        else:
            print("Составное")
        return result  # Возвращаем результат
    return wrapper

# Функция, которая складывает три числа
@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)  # Вывод результата
