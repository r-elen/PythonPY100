speed = 4096  # скорость передачи данных в байтах/cек
time = 120  # время в минутах затраченное на скачивание игры
cost = 5  # стоимость за один мегабайт

# TODO рассчитайте размер и стоимость файла
free_trafic = 10

time_sec = 120 * 60
file_size_b = speed * time_sec

file_size = file_size_b / 1024 / 1024  # размер файла
total_coast = (file_size - free_trafic) * 5  # стоимость файла

print(f'Размер файла в мегабайтах =', file_size)
print(f'За трафик придется заплатить:', total_coast)
