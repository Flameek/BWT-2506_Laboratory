import math
import datetime

def f():
    try:
        number = int(input("Введите число:"))
        if number < 0:
            print(f"Число отрицательное")
            return
        x = math.sqrt(number)
        print(f"Квадратный корень из {number} = {x}")
        return True
    except ValueError:
        print("Введено не число")
        return False
        

def g():
    now = datetime.datetime.now()
    print(f"Здравствуйте. С вами программа ввести. Сегодня {now}")

print('1 задание')
if f():
    g()
