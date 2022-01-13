import random
a = random.randint(100,1000)
print(a)
p = a % 10
b = a//10
c = b % 10
k = b//10
print('Сумму трех цифр случайного трехзначного числа:',p+c+k)