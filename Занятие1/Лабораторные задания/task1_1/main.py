DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input('Год рождения: '))  # TODO запросить у пользователя год рождения
current_year = int(input('Текущий год: '))  # TODO запросить у пользователя текущий год

print((current_year - start_year) * DAYS_OF_YEAR) # TODO посчитать и распечатать количество прожитых дней
