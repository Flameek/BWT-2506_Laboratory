class Circle:
    def __init__(self, radius):
        self.radius = radius # Конструктор для инициализации радиуса круга
        
    
    def get_radius(self):
        return self.radius #Возвращает значение радиуса круга
    
    def set_radius(self, new_radius):
        self.radius = new_radius # Позволяет менять значение радиуса круга
        
# Создание круга с проверкой
while True:
    try:
        radius = float(input("Введите радиус круга: "))
        if radius < 0:
            print("Ошибка: Радиус не может быть отрицательным!")
        else:
            break
    except ValueError:
        print("Ошибка: Введите число!")

circle = Circle(radius)
print(f"Текущий радиус: {circle.get_radius()}")

# Меняем радиус с проверкой
while True:
    try:
        new_radius = float(input("Введите значение нового радиуса круга: "))
        if new_radius < 0:
            print("Радиус не может быть отрицательным!")
        else:
            break
    except ValueError:
        print("Введено число!")

circle.set_radius(new_radius)
print(f"Новый радиус: {circle.get_radius()}")
        
