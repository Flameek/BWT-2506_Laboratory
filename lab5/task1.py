class Book:
    def __init__(self, title, author, year):
        self. title = title
        self.author = author
        self.year = year
    
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания; {self.year}"

# бесконечный цикл добавления книг и их автором, названием и годом издания
books = [] #Для хранения книг

while True:
    print("Библиотека книг!")
    #Ввод названия книг с проверкой
    while True:
        title = input("Введите название книги:")
        if not title.strip():
            print("Название не может быть путсым")
        if len(title.strip()) <= 2:
            print("Название не может содержать в себе меньше двух символов")
        else:
            title = title.strip()
            break
        
    # Ввод имени автора с проверкой
    while True:
        author = input("Введите Фамилию И.О. автора (И.О. - можно инциалами): ")
        if not author.strip():
            print("Имя автора не может быть пустым!")
        if len(author.strip()) <= 2:
            print("Имя не может содержать в себе меньше двух символов")
        else:
            author = author.strip()
            break
        
    # Ввод года издания с проверкой
    while True:
        year_inp = input("Введите год издания: ")
        try:
            year = int(year_inp)
            if year < 1000:
                print("Год издания не может быть раньше 1000-го года")
            if year > 2025:
                print("Год не может быть больше 2025 года!")
            else:
                break
        except ValueError:
            print("Год должен быть числом")

    book = Book(title,author,year)
    books.append(book)

    print(f"Добавлена книга: {book.get_info()}")
    print("Ваша библиотека:")
    for i, book_1 in enumerate(books, 1):
        print(f"{i}. {book_1.get_info()}")
        
    try:
        continue_choice = input("\nХотите добавить еще книгу? (да/нет): ").lower()
        if continue_choice != 'да':
            print("Программа завершена!")
            break
    except EOFError:
        print("\nПрограмма завершена!")
        break

     