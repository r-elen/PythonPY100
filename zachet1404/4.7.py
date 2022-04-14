import random

list_nums = []
while len(set(list_nums)) < 20:
    list_nums = [random.randint(-100, 100) for _ in range(20)]


while True:
    list_nums = [random.randint(-100, 100) for _ in range(20)]
    if len(set(list_nums)) == 20:
        break


print(set(list_nums), f'\nКолличество элементов - {len(set(list_nums))}')
