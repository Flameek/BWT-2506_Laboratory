"""
Лабораторная работа №7. Работа с классами ч.3
Система управления сотрудниками с множественным наследованием
"""

# 1. Базовый класс Employee
class Employee:
    """
    Базовый класс для всех сотрудников.
    Демонстрирует инкапсуляцию через свойства (property).
    """
    def __init__(self, name: str, emp_id: str):
        # Инкапсуляция: атрибуты защищены (private)
        self._name = name
        self._emp_id = emp_id
    
    # Геттеры для доступа к защищенным атрибутам
    @property
    def name(self):
        return self._name
    
    @property
    def emp_id(self):
        return self._emp_id
    
    def get_info(self) -> str:
        """Возвращает базовую информацию о сотруднике (полиморфизм)"""
        return f"Сотрудник: {self._name}, ID: {self._emp_id}"
    
    def work(self) -> str:
        """Абстрактный метод для демонстрации полиморфизма"""
        return f"{self._name} выполняет свою работу."


# 2. Класс Manager
class Manager(Employee):
    """
    Класс менеджера. Наследуется от Employee.
    Добавляет управленческие функции.
    """
    def __init__(self, name: str, emp_id: str, department: str):
        # Вызываем конструктор родительского класса
        super().__init__(name, emp_id)
        # Инкапсуляция: защищенный атрибут
        self._department = department
        # Приватный список подчиненных
        self.__subordinates = []
    
    @property
    def department(self):
        return self._department
    
    def manage_project(self, project_name: str) -> str:
        """Метод для управления проектами"""
        return f"Менеджер {self.name} управляет проектом '{project_name}' в отделе {self._department}"
    
    def work(self) -> str:
        """Переопределение метода work (полиморфизм)"""
        return f"{self.name} руководит отделом {self._department}"
    
    def get_info(self) -> str:
        """Расширение метода get_info"""
        base_info = super().get_info()
        return f"{base_info}, Должность: Менеджер, Отдел: {self._department}"


# 3. Класс Technician
class Technician(Employee):
    """
    Класс технического специалиста. Наследуется от Employee.
    Добавляет технические навыки.
    """
    def __init__(self, name: str, emp_id: str, specialization: str):
        super().__init__(name, emp_id)
        self._specialization = specialization
    
    @property
    def specialization(self):
        return self._specialization
    
    def perform_maintenance(self) -> str:
        """Метод для выполнения технического обслуживания"""
        return f"Техник {self.name} выполняет обслуживание в области {self._specialization}"
    
    def work(self) -> str:
        """Переопределение метода work (полиморфизм)"""
        return f"{self.name} работает над технической задачей в области {self._specialization}"
    
    def get_info(self) -> str:
        """Расширение метода get_info"""
        base_info = super().get_info()
        return f"{base_info}, Должность: Техник, Специализация: {self._specialization}"


# 4. Класс TechManager (множественное наследование)
class TechManager(Manager, Technician):
    """
    Класс технического менеджера.
    Наследуется от Manager и Technician (множественное наследование).
    Комбинирует управленческие и технические навыки.
    """
    def __init__(self, name: str, emp_id: str, department: str, specialization: str):
        # Используем MRO (Method Resolution Order) для правильного вызова конструкторов
        # Вызываем конструктор Manager (первый в списке наследования)
        Manager.__init__(self, name, emp_id, department)
        # Инициализируем атрибуты Technician
        self._specialization = specialization
    
    # 5. Метод для добавления сотрудников
    def add_employee(self, employee: Employee) -> None:
        """Добавляет сотрудника в список подчиненных"""
        if employee not in self._Manager__subordinates:  # Доступ к приватному атрибуту
            self._Manager__subordinates.append(employee)
            print(f"{employee.name} добавлен в команду {self.name}")
        else:
            print(f"{employee.name} уже в команде {self.name}")
    
    # 6. Метод для получения информации о команде
    def get_team_info(self) -> str:
        """Возвращает информацию о всех подчиненных"""
        if not self._Manager__subordinates:
            return f"У {self.name} нет подчиненных"
        
        team_info = [f"Команда {self.name} ({len(self._Manager__subordinates)} чел.):"]
        for i, emp in enumerate(self._Manager__subordinates, 1):
            team_info.append(f"{i}. {emp.get_info()}")
        return "\n".join(team_info)
    
    def work(self) -> str:
        """Переопределение метода work для TechManager"""
        return f"{self.name} совмещает управление отделом {self.department} и техническую работу в области {self.specialization}"
    
    def get_info(self) -> str:
        """Переопределение метода get_info"""
        return f"{super().get_info()}, Специализация: {self.specialization}"
    
    def manage_and_maintain(self, project_name: str) -> str:
        """Уникальный метод TechManager - совмещает управление и техническую работу"""
        manage_msg = self.manage_project(project_name)
        tech_msg = self.perform_maintenance()
        return f"{manage_msg}\n{tech_msg}"


# Демонстрация функциональности
def main():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ СИСТЕМЫ УПРАВЛЕНИЯ СОТРУДНИКАМИ")
    print("=" * 60)
    
    # Создание объектов разных классов
    print("\n1. СОЗДАНИЕ СОТРУДНИКОВ:")
    print("-" * 40)
    
    # Базовый сотрудник
    emp1 = Employee("Иван Иванов", "EMP001")
    print(emp1.get_info())
    
    # Менеджер
    manager1 = Manager("Анна Петрова", "MGR001", "Разработка")
    print(manager1.get_info())
    
    # Техник
    tech1 = Technician("Петр Сидоров", "TECH001", "Сетевое оборудование")
    print(tech1.get_info())
    
    # Технический менеджер (множественное наследование)
    tech_manager = TechManager(
        "Сергей Козлов", 
        "TM001", 
        "ИТ-инфраструктура", 
        "Системное администрирование"
    )
    print(tech_manager.get_info())
    
    # 7. Демонстрация полиморфизма
    print("\n2. ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА (метод work()):")
    print("-" * 40)
    
    employees = [emp1, manager1, tech1, tech_manager]
    for emp in employees:
        print(f"• {emp.work()}")
    
    # Демонстрация уникальных методов
    print("\n3. УНИКАЛЬНЫЕ МЕТОДЫ КЛАССОВ:")
    print("-" * 40)
    
    print(f"• {manager1.manage_project('Внедрение CRM')}")
    print(f"• {tech1.perform_maintenance()}")
    print(f"• {tech_manager.manage_and_maintain('Обновление серверов')}")
    
    # Работа с подчиненными
    print("\n4. УПРАВЛЕНИЕ КОМАНДОЙ:")
    print("-" * 40)
    
    # Добавление сотрудников в команду tech_manager
    tech_manager.add_employee(manager1)
    tech_manager.add_employee(tech1)
    tech_manager.add_employee(emp1)
    
    # Попытка добавить уже существующего сотрудника
    tech_manager.add_employee(tech1)
    
    # Вывод информации о команде
    print("\n" + tech_manager.get_team_info())
    
    # Проверка MRO (Method Resolution Order)
    print("\n5. ПОРЯДОК РАЗРЕШЕНИЯ МЕТОДОВ (MRO):")
    print("-" * 40)
    print("Порядок наследования для TechManager:")
    for i, cls in enumerate(TechManager.__mro__, 1):
        print(f"{i}. {cls.__name__}")
    
    # Демонстрация инкапсуляции
    print("\n6. ДЕМОНСТРАЦИЯ ИНКАПСУЛЯЦИИ:")
    print("-" * 40)
    print(f"Доступ через свойства (property): {tech_manager.name}")
    print(f"Доступ к отделу: {tech_manager.department}")
    print(f"Доступ к специализации: {tech_manager.specialization}")
    
    # Прямой доступ к защищенным атрибутам (не рекомендуется, но возможен)
    print(f"\nПрямой доступ к защищенным атрибутам (не рекомендуется):")
    print(f"Защищенный атрибут _name: {tech_manager._name}")
    
    # Попытка доступа к приватному атрибуту
    print(f"\nПопытка доступа к приватному атрибуту __subordinates:")
    try:
        print(tech_manager.__subordinates)
    except AttributeError as e:
        print(f"Ошибка: {e}")
        print("Это демонстрирует инкапсуляцию - приватные атрибуты недоступны извне")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()