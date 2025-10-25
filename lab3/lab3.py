#1,3
def read_file(path='example.txt', mode='all'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            if mode == 'all':
                content = f.read()
                print("Чтение всего файла сразу:\n")
                print(content)
            elif mode == 'line':
                print("Чтение файла построчно:\n")
                for i, line in enumerate(f, start=1):
                    print(f"{i}: {line.strip()}")
            else:
                print('Неверный тип чтения')
    except FileNotFoundError:
        print('Файл не найден')

def main():
    print("Лаба 1: Задания 1 и 3")
    print("Работа с файлами\n")

    filename = "lab3/example.txt"
    mode = input("Выберите тип чтения (all / line): ")

    read_file(filename, mode)

main()
#2
def write_to_file(filename='user_input.txt', append=False):
    try:
        text = input("Введите текст для записи:")
        mode = 'a' if append else 'w'
        with open(filename, mode, encoding='utf8') as f:
            f.write(text + '\n')
        if append:
            print(f"Текст добавлен в существующий файл {filename}")
        else:
            print(f"Файл {filename} создан и текст записан")
    except PermissionError:
        print("Ошибка: нет доступа для записи в файл.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def main():
    print("Лаба 3: Задание 2 - добавление и запись в файл")
    while True:
        choice = input('Вы хотите созать новый файл (1) или добавить текст (2) или 3 чтобы остановить')
        if choice == '1':
            write_to_file(append=False)
        elif choice == '2':
            write_to_file(append=True)
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор: Введите 1 или 2 или 3")
main()