
a = int(input())
b = int(input())

sum_kv = a**2 + b**2
kv_sum = (a+b)**2

if sum_kv > kv_sum:
    print("Сумма квадратов больше")
elif sum_kv < kv_sum:
    print("Квадрат суммы больше")
else:
    print("Значения равны")
