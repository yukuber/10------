import sqlite3

# Создание или подключение к базе данных SQLite
db_connection = sqlite3.connect('example.db')
cursor = db_connection.cursor()

# Шаг 1: Создание таблицы
create_table_query = """
CREATE TABLE IF NOT EXISTS Students (
    st_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    st_name TEXT NOT NULL,
    st_surname TEXT NOT NULL,
    st_date_of_birth DATE NOT NULL,
    st_department TEXT NOT NULL
    )
"""
cursor.execute(create_table_query)
print("Таблица 'Students' успешно создана.")

create_table_query = """
CREATE TABLE IF NOT EXISTS Teachers (
    te_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    te_name TEXT NOT NULL,
    te_surname TEXT NOT NULL,
    te_department TEXT NOT NULL
    )
"""
cursor.execute(create_table_query)
print("Таблица 'Teachers' успешно создана.")

create_table_query = """
CREATE TABLE IF NOT EXISTS Courses (
    co_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    co_title TEXT NOT NULL,
    co_description TEXT NOT NULL,
    te_id INT,
    FOREIGN KEY (te_id) REFERENCES Teachers(te_id)
    )
"""
cursor.execute(create_table_query)
print("Таблица 'Courses' успешно создана.")

create_table_query = """
CREATE TABLE IF NOT EXISTS Exams (
    ex_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    ex_date DATE NOT NULL,
    co_id INT,
    ex_max_score INTEGER NOT NULL,
    FOREIGN KEY (co_id) REFERENCES Courses(co_id)
    )
"""

cursor.execute(create_table_query)
print("Таблица 'Exams' успешно создана.")

create_table_query = """
CREATE TABLE IF NOT EXISTS Grades (
    gr_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    st_id INT,
    ex_id INT,
    FOREIGN KEY (st_id) REFERENCES Students(st_id),
    FOREIGN KEY (ex_id) REFERENCES Exams(ex_id)
    )
"""
cursor.execute(create_table_query)
print("Таблица 'Grades' успешно создана.")

# Шаг 2: Вставка данных
def add_student(name, surname, department, date_of_birth):
    cursor.execute('INSERT INTO Students (st_name, st_surname, st_department, st_date_of_birth) VALUES (?, ?, ?, ?)', (name, surname, department, date_of_birth))
    db_connection.commit()

def add_teacher(name, surname, department):
    cursor.execute('INSERT INTO Teachers (te_name, te_surname, te_department) VALUES (?, ?, ?)', (name, surname, department))
    db_connection.commit()

def add_course(title, description, teacher_id):
    cursor.execute('INSERT INTO Courses (co_title, co_description, te_id) VALUES (?, ?, ?)', (title, description, teacher_id))
    db_connection.commit()
def update_student(student_id, name=None, surname=None, date_of_birth=None):
    if name:
        cursor.execute("UPDATE Students SET st_name = ? WHERE st_id = ?", (name, student_id))
    if surname:
        cursor.execute("UPDATE Students SET st_surname = ? WHERE st_id = ?", (surname, student_id))
    if date_of_birth:
        cursor.execute("UPDATE Students SET st_date_of_birth = ? WHERE st_id = ?", (date_of_birth, student_id))
    db_connection.commit()
def update_teacher(te_id, name=None, surname=None, date_of_birth=None):
    if name:
        cursor.execute("UPDATE Teachers SET te_name = ? WHERE te_id = ?", (name, te_id))
    if surname:
        cursor.execute("UPDATE Students SET te_surname = ? WHERE te_id = ?", (surname, te_id))
    if date_of_birth:
        cursor.execute("UPDATE Students SET te_department = ? WHERE te_id = ?", (date_of_birth, te_id))
    db_connection.commit()


while True:
    print("Выберите действие:")
    print("1. Добавить нового студента")
    print("2. Добавить нового преподавателя")
    print("3. Добавить новый курс")
    print('4. Изменить данные о студенте')
    print('5. Изменить данные об учителе')


    choice = input("Введите номер действия (или 'exit' для выхода): ")

    if choice == 'exit':
        break
    elif choice == '1':
        name = input("Введите имя студента: ")
        surname = input("Введите фамилию студента: ")
        department = input("Введите факультет студента: ")
        date_of_birth = input("Введите дату рождения студента (гггг-мм-дд): ")
        add_student(name, surname, department, date_of_birth)
    elif choice == '2':
        name = input("Введите имя преподавателя: ")
        surname = input("Введите фамилию преподавателя: ")
        department = input("Введите кафедру преподавателя: ")
        add_teacher(name, surname, department)
    elif choice == '3':
        title = input("Введите название курса: ")
        description = input("Введите описание курса: ")
        teacher_id = int(input("Введите ID преподавателя курса: "))
        add_course(title, description, teacher_id)
   
    elif choice == '4':
        choice1 = input('Введите тип данных для обновления (name, surname, date_of_birth) or exit ')
        while choice1 != 'exit':
            student_id = int(input('Введите id студента '))
            if choice1 == 'name':
                name = input('Введите новое имя ')
                update_student(student_id, name)
            elif choice1 == 'surname':
                surname = input('Введите новую фамилию ')
                update_student(student_id, surname)
            elif choice1 == 'date_of_birth':
                date_of_birth = input('Введите новую дату ')
                update_student(student_id, date_of_birth)
            choice1 = input('Введите тип данных для обновления (name, surname, date_of_birth) or exit ')
    elif choice == '5':
        choice1 = input('Введите тип данных для обновления (name, surname, department) or exit ')
        while choice1 != 'exit':
            student_id = int(input('Введите id учителя'))
            if choice1 == 'name':
                name = input('Введите новое имя')
                update_student(student_id, name)
            elif choice1 == 'surname':
                surname = input('Введите новую фамилию')
                update_student(student_id, surname)
            elif choice1 == 'date_of_birth':
                date_of_birth = input('Введите новый факультет')
                update_student(student_id, date_of_birth)
    choice1 = input('Введите тип данных для обновления (name, surname, department) or exit ')
db_connection.close()

# Шаг 3: Выборка данных
select_query = "SELECT * FROM Users"
cursor.execute(select_query)
result = cursor.fetchall()
print("\nДанные в таблице 'Users':")
for row in result:
    print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# Шаг 4: Обновление данных

# Шаг 5: Выборка данных после обновления
cursor.execute(select_query)
result = cursor.fetchall()
print("\nДанные в таблице 'Users' после обновления:")
for row in result:
    print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# Шаг 6: Удаление данных
delete_query = "DELETE FROM Users WHERE name = ?"
user_to_delete = ("Alice Johnson",)
cursor.execute(delete_query, user_to_delete)
db_connection.commit()
print(f"Пользователь 'Alice Johnson' успешно удален.")

# Шаг 7: Окончательная выборка данных после удаления
cursor.execute(select_query)
result = cursor.fetchall()
print("\nДанные в таблице 'Users' после удаления:")
for row in result:
    print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# Закрытие соединения
cursor.close()
db_connection.close()
print("\nСоединение с базой данных закрыто.")
