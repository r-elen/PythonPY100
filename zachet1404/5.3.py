a = int(input())

list_digits = [int(d) for d in str(a)]
list_digs_even = [d for d in list_digits if d % 2 == 0]
list_digs_odd = [int(d) for d in str(a) if int(d) % 2 != 0]
print(f'Четных: {len(list_digs_even)} \nНечетных: {len(list_digs_odd)}')
