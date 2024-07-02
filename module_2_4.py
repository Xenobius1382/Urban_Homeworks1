# закрепление навыков решения задач при помощи цикла for, применение знаний об основных типах данных

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] # список с простыми числами
not_primes = [] # список с составными числами
is_prime = True # переменная флаг меняющая значение в зависимости от типа числа
check = 0 # переменная для реализации итерации вложенного цикла перебора делителей числа
for i in numbers:
    if i > 1:
        for k in range(2, i // 2+1):
            check = 0
            if (i % k == 0):
              check = check + 1
        if (check <= 0):
            is_prime = True
        else:
            is_prime = False
        if (is_prime == True):
            primes.append(i)
        else:
            not_primes.append(i)
print(primes)
print(not_primes)






