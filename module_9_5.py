# Создаем пользовательский класс исключения StepValueError
class StepValueError(ValueError):
    pass  # Оставляем класс пустым, так как дополнительная логика не требуется


# Класс Iterator
class Iterator:
    def __init__(self, start, stop, step=1):
        # Проверка на корректность шага
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Устанавливаем pointer в начало

    def __iter__(self):
        # Метод __iter__ возвращает итератор и сбрасывает pointer на start
        self.pointer = self.start
        return self

    def __next__(self):
        # Метод __next__ увеличивает pointer на step и завершает итерацию, если достигнут конец
        if self.step > 0 and self.pointer > self.stop:  # Когда step положителен
            raise StopIteration
        elif self.step < 0 and self.pointer < self.stop:  # Когда step отрицателен
            raise StopIteration

        current_value = self.pointer  # Сохраняем текущее значение pointer
        self.pointer += self.step  # Увеличиваем pointer на step
        return current_value


# Пример использования:
try:
    iter1 = Iterator(100, 200, 0)  # Попытка с шагом 0
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

# Другие примеры итераторов:
iter2 = Iterator(-5, 1)  # Шаг по умолчанию = 1
iter3 = Iterator(6, 15, 2)  # Шаг = 2
iter4 = Iterator(5, 1, -1)  # Шаг = -1
iter5 = Iterator(10, 1)  # Шаг по умолчанию = 1

# Итерация по iter2
for i in iter2:
    print(i, end=' ')
print()

# Итерация по iter3
for i in iter3:
    print(i, end=' ')
print()

# Итерация по iter4
for i in iter4:
    print(i, end=' ')
print()

# Итерация по iter5
for i in iter5:
    print(i, end=' ')
print()
