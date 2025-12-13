class Employee:  # Класс с общими атрибутами для сотрудников
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        self._active = True  # Частная переменная для статуса сотрудника

    def get_info(self):
        return f"ID: {self.id}, Имя: {self.name}, Зарплата: {self.salary}"

    def get_role(self):
        return self.__class__.__name__

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def status(self):
        return "Сотрудник активен" if self._active else "Сотрудник неактивен"

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, id, salary, department, projects=None, team=None):
        super().__init__(name, id, salary)
        self.department = department
        self.projects = projects if projects is not None else []
        self.team = team if team is not None else []

    def manage_project(self, project_name):
        self.projects.append(project_name)
        return f"Проект '{project_name}' добавлен в отдел {self.department}"

    def add_to_team(self, employee):
        self.team.append(employee)
        return f"Сотрудник {employee.name} добавлен в команду менеджера {self.name}"

    def remove_from_team(self, employee):
        if employee in self.team:
            self.team.remove(employee)
            return f"Сотрудник {employee.name} уволен из команды менеджера {self.name}"
        else:
            return f"Сотрудник {employee.name} не найден в команде {self.name}"

    def get_team_info(self):
        if not self.team:
            return "Команда пуста"
        return "\n".join(emp.get_info() for emp in self.team)

    def calculate_salary(self):
        return self.salary * 1.2  # пример управленческой надбавки


class Technician(Employee):
    def __init__(self, name, id, salary, specialization, certifications=None):
        super().__init__(name, id, salary)
        self.specialization = specialization
        self.certifications = certifications if certifications is not None else []

    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание ({self.specialization})"

    def add_certification(self, cert):
        self.certifications.append(cert)
        return f"Сертификат '{cert}' добавлен для {self.name}"

    def calculate_salary(self):
        return self.salary * 1.1  # пример технической надбавки


class TechManager(Manager, Technician):
    def __init__(self, name, id, salary, department, specialization,
                 projects=None, team=None, technical_projects=None):
        # Явно инициализируем базовые поля от Employee
        Employee.__init__(self, name, id, salary)
        # затем задаём специфичные поля
        self.department = department
        self.specialization = specialization
        self.projects = projects if projects is not None else []
        self.team = team if team is not None else []
        self.technical_projects = technical_projects if technical_projects is not None else []

    def manage_project(self, project_name):
        self.projects.append(project_name)
        return f"Технический менеджер {self.name} добавил проект '{project_name}' в отдел {self.department}"

    def perform_maintenance(self):
        return f"{self.name} (TechManager) выполняет техническое обслуживание ({self.specialization})"

    def assign_task(self, employee, task):
        task.assign(employee)
        return f"Задача '{task.title}' назначена сотруднику {employee.name} менеджером {self.name}"

    def calculate_salary(self):
        return self.salary * 1.35  # комбинированная надбавка


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.assigned_to = None
        self.status = "Создана"  # Создана / Назначена / В работе / Выполнена

    def assign(self, employee):
        self.assigned_to = employee
        self.status = "Назначена"

    def start(self):
        if self.assigned_to is not None:
            self.status = "В работе"

    def complete(self):
        self.status = "Выполнена"

    def __str__(self):
        assigned = self.assigned_to.name if self.assigned_to else "Не назначена"
        return f"Задача: {self.title} | Описание: {self.description} | Выполнитель: {assigned} | Статус: {self.status}"


class EmployeeRegistry:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.id] = employee

    def remove_employee(self, employee_id):
        return self.employees.pop(employee_id, None)

    def get_employee(self, employee_id):
        return self.employees.get(employee_id)

    def get_all_employees(self):
        return list(self.employees.values())

    def get_employees_by_role(self, role_name):
        return [emp for emp in self.employees.values() if emp.__class__.__name__ == role_name]


if __name__ == "__main__":
    # Примеры использования (демонстрация)
    registry = EmployeeRegistry()

    emp1 = Employee("Иван", 1, 50000)
    emp2 = Employee("Мария", 2, 52000)

    manager = Manager("Анна", 3, 70000, "IT")
    tech = Technician("Сергей", 4, 60000, "Сети")
    tech_mgr = TechManager("Ольга", 5, 90000, "Разработка", "Backend")

    registry.add_employee(emp1)
    registry.add_employee(emp2)
    registry.add_employee(manager)
    registry.add_employee(tech)
    registry.add_employee(tech_mgr)

    print(manager.add_to_team(emp1))
    print(manager.add_to_team(emp2))
    print("Команда менеджера Анна:")
    print(manager.get_team_info())
    print()

    print(manager.manage_project("CRM система"))
    print(tech.perform_maintenance())
    print(tech.add_certification("Cisco CCNA"))
    print()

    task = Task("Настройка сервера", "Установить и настроить Nginx")
    print(tech_mgr.assign_task(tech, task))
    print(task)
    task.start()
    print("После старта:", task)
    task.complete()
    print("После завершения:", task)
    print()

    # Полиморфизм: разные calculate_salary для разных ролей
    print("--- Зарплаты ---")
    for emp in registry.get_all_employees():
        print(f"{emp.name} ({emp.get_role()}): {emp.calculate_salary()}")

        
    