def apply_all_func(int_list, *functions):
    # Создаём пустой словарь для результатов
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        # Вызываем функцию с int_list и сохраняем результат под её именем
        results[func.__name__] = func(int_list)

    # Возвращаем словарь с результатами
    return results


# Примеры использования:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
