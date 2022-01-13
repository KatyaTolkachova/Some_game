a = int(input("Введите дату дня рождения:"))
b = int(input("Введите месяц дня рождения:"))
h = int(input("Введите год дня рождения:"))
if (a >= 21 and b == 1) or (a <= 19 and b == 2):
    print("Водолей")
elif (a >= 20 and b == 2) or (a <= 20 and b == 3):
    print("Рыба")
elif (a >= 21 and b == 3) or (a <= 20 and b == 4):
    print("Овен")
elif (a >= 21 and b == 4) or (a <= 21 and b == 5):
    print("Телец")
elif (a >= 22 and b == 5) or (a <= 21 and b == 6):
    print("Близнец")
elif (a >= 22 and b == 6) or (a <= 22 and b == 7):
    print("Рак")
elif (a >= 23 and b == 7) or (a <= 21 and b == 8):
    print("Лев")
elif (a >= 22 and b == 8) or (a <= 23 and b == 9):
    print("Дева")
elif (a >= 24 and b == 9) or (a <= 23 and b == 10):
    print("Весы")
elif (a >= 24 and b == 10) or (a <= 22 and b == 11):
    print("Скорпион")
elif (a >= 23 and b == 11) or (a <= 22 and b == 12):
    print("Стрелец")
elif (a >= 23 and b == 12) or (a <= 20 and b == 1):
    print("Козерог")
else:
    print("Ошибка")
d = int(input("Введите сегодняшний день:"))
m = int(input("Введите сегодняшний месяц:"))
y = int(input("Введите сегодняшний год:"))
if (a < d and b <= m) or (a == d and b < m):
    print("Возраст:", y - h)
elif (a < d and b > m) or (a == d and b < m):
    print("Возраст:", y - h - 1)
elif a > d and b < m:
    print("Возраст:", y - h)
elif (a == d and b > m) or (a > d and b >= m ):
    print("Возраст:", y - h - 1)
elif a == d and b == m:
    print("Сегодня День Рождения:", y - h)
