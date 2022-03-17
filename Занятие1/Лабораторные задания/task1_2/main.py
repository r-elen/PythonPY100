NALOG_PROCENT = 0.13
salary = int(input("Зарплата: "))

nalog = salary * NALOG_PROCENT
real_salary = salary - nalog

print(nalog, real_salary)
