import asyncio


# Асинхронная функция для имитации соревнований по поднятию шаров Атласа
async def start_strongman(name, power):
    # Вывод сообщения о начале соревнований
    print(f'Силач {name} начал соревнования.')
    # Цикл для имитации поднятия шаров
    for i in range(1, 6):
        # Задержка, обратно пропорциональная силе силача
        await asyncio.sleep(1 / power)
        # Вывод сообщения о поднятии шара
        print(f'Силач {name} поднял {i} шар')
    # Вывод сообщения о завершении соревнований
    print(f'Силач {name} закончил соревнования.')


# Асинхронная функция для запуска турнира
async def start_tournament():
    # Создание задач для функции start_strongman с разными именами и силами
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    # Постановка задач в режим ожидания
    await task1
    await task2
    await task3


# Запуск асинхронной функции start_tournament
asyncio.run(start_tournament())
