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
    def __init__(self, name, id, salary, spezialization, sertifications=None):
        super().__init__(name, id, salary)
        self.spezialization = spezialization
        self.sertifications = sertifications if sertifications is not None else []
    
    def perform_maintenance(self):
        return f"{self.name} Выполняет техническое обслуживание в обслати {self.spezialization}"

    def add_sertifications(self, sert):
        self.sertifications.append(sert)
    
    def calculate_salary(self):
        return self.salary * 1.1


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, salary, department, specialization, technical_projects=None):
        Manager.__init__(self, name, id, salary, department)
        Technician.__init__(self, name, id, salary, specialization)
        self.technical_projects = technical_projects if technical_projects is not None else []
    
    def manage_project(self, project_name):
        return Manager.manage_project(self, project_name)
    
    def perform_maintenance(self):
        return Technician.perform_maintenance(self)
    
    def assign_task(self, employee, task):
        if employee in self.team:
            return f"TechManager {self.name}, назначил задачу '{task.title}' сотруднику {employee.name}"
        return f"{employee.name} не в команде"
    
    def add_employee(self, employee):
        return Manager.add_to_team(self, employee)
    
    def get_team_info(self):
        return Manager.get_team_info(self)
    
    def calculate_salary(self):
        manager_salary = Manager.calculate_salary(self) 
        tech_salary = Technician.calculate_salary(self)
        return (manager_salary + tech_salary) / 2
    
    def get_info(self):
        return f"TechManager: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.spezialization}"
        
def main():
    print("Система управления сотрудниками")

    # Создание менеджера
    manager_name = input("Введите имя менеджера: ")
    department = input("Введите отдел: ")
    manager = Manager(manager_name, 1, 1000, department)

    while True:
        print("\nМеню:")
        print("1 - Добавить сотрудника")
        print("2 - Добавить проект")
        print("3 - Показать команду")
        print("4 - Показать зарплаты")
        print("0 - Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            emp_name = input("Имя сотрудника: ")
            emp_salary = int(input("Зарплата сотрудника: "))
            employee = Employee(emp_name, len(manager.team) + 2, emp_salary)
            print(manager.add_to_team(employee))

        elif choice == "2":
            project = input("Название проекта: ")
            print(manager.manage_project(project))

        elif choice == "3":
            print("Команда менеджера:")
            print(manager.get_team_info())

        elif choice == "4":
            print("Зарплаты:")
            print(f"{manager.name} (Manager): {manager.calculate_salary()}")
            for emp in manager.team:
                print(f"{emp.name} (Employee): {emp.calculate_salary()}")

        elif choice == "0":
            print("Выход из программы")
            break

        else:
            print("Неверный ввод")


if __name__ == "__main__":
    main()

        
    