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
    st_date_of_birth TEXT NOT NULL,
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
    gr_score INT,
    FOREIGN KEY (st_id) REFERENCES Students(st_id),
    FOREIGN KEY (ex_id) REFERENCES Exams(ex_id)
    )
"""
cursor.execute(create_table_query)
print("Таблица 'Grades' успешно создана.")


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

def update_cource(co_id, title=None, description=None, te_id=None):
    if name:
        cursor.execute("UPDATE Cources SET co_title = ? WHERE co_id = ?", (title, co_id))
    if surname:
        cursor.execute("UPDATE Cources SET co_description = ? WHERE co_id = ?", (description, co_id))
    if date_of_birth:
        cursor.execute("UPDATE Couces SET te_id = ? WHERE Co_id = ?", (te_id, co_id))
    db_connection.commit()


def delete_student(student_id):
    cursor.execute('DELETE FROM Students WHERE st_id ='+student_id)

def delete_teacher(teacher_id):
    cursor.execute('DELETE FROM Teachers WHERE te_id ='+teacher_id)

def delete_cource(cource_id):
    cursor.execute('DELETE FROM Cources WHERE co_id ='+cource_id)


def get_students_by_department(department):
    cursor.execute(f"SELECT st_id, st_name, st_surname FROM Students WHERE st_department = '{department}'")
    result = cursor.fetchall()
    print(f'Факультет "{department}"')
    for row in result:
        print(f'ID:{row[0]}----Имя:{row[1]}----Фамилия:{row[2]}')
    print('\n')

def get_teacher_courses(teacher_id):
    cursor.execute(f"SELECT co_id, co_title, co_description FROM Courses WHERE te_id = {teacher_id}")
    result = cursor.fetchall()
    print(f'Преподаватель с ID {teacher_id}')
    for row in result:
        print(f"ID курса:{row[0]}----Название:{row[1]}----Описание:{row[2]}")
    print("\n")

def get_grades(student_id):
    cursor.execute(f"SELECT ex_id, gr_score FROM Grades WHERE st_id = {student_id}")
    result = cursor.fetchall()
    print(f"Успеваемость студента с ID {student_id}")
    for row in result:
        print(f"ID экзамена:{row[0]}----Оценка:{row[1]}")
    print("\n")


def average_student(student_id):
    cursor.execute(f"SELECT avg(gr_score) FROM Grades WHERE st_id = {student_id}")
    res = cursor.fetchall()
    print(f"Средний балл студента с ID {student_id}: {res[0][0]}\n")

def average_of_department(department):
    cursor.execute(f"""SELECT avg(gr_score)
        FROM Students s
        JOIN Grades g on s.id = g.student_id
        WHERE department = '{department}'""")
    res = cursor.fetchall()
    print(f"Средний балл по факультету {department}: {res[0][0]}\n")

while True:
    # try:

    print("Выберите действие:")
    print("1. Добавить нового студента")
    print("2. Добавить нового преподавателя")
    print("3. Добавить новый курс")
    print()
    print('4. Изменить данные о студенте')
    print('5. Изменить данные об учителе')
    print('6. Изменить данные о курсе')
    print()
    print('7. Удалить студента')
    print('8. Удалить преподавателя')
    print('9. Удалить курс')
    print()
    print('10. Вывод списка студентов по курсу')
    print('11. Вывод курса преподавателя')
    print('12. Вывод оценок студента')
    print()
    print('13. Расчет среднего балла студента')
    print('14. Расчет среднего балла по курсу')


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
                update_student(name, student_id)
            elif choice1 == 'surname':
                surname = input('Введите новую фамилию ')
                update_student(surname, student_id)
            elif choice1 == 'date_of_birth':
                date_of_birth = input('Введите новую дату ')
                update_student(date_of_birth, student_id)
            choice1 = input('Введите тип данных для обновления (name, surname, date_of_birth) or exit ')
    elif choice == '5':
        choice1 = input('Введите тип данных для обновления (name, surname, department) or exit ')
        while choice1 != 'exit':
            te_id = int(input('Введите id учителя'))
            if choice1 == 'name':
                name = input('Введите новое имя')
                update_student(name, te_id)
            elif choice1 == 'surname':
                surname = input('Введите новую фамилию')
                update_student(surname, te_id )
            elif choice1 == 'department':
                department = input('Введите новый факультет')
                update_student( department, te_id)
            choice1 = input('Введите тип данных для обновления (name, surname, department) or exit ')
    elif choice == '6':
        choice1 = input('Введите тип данных для обновления (title, description, teacher_id) or exit ')
        while choice1 != 'exit': 
            co_id = int(input('Введите id курса '))
            if choice1 == 'title':
                title = input('Введите новое название: ')
                update_student(title, co_id )
            elif choice1 == 'description':
                description = input('Введите новое описание: ')
                update_student(description, co_id)
            elif choice1 == 'date_of_birth':
                te_id = input('Введите id нового преподавателя: ')
                update_student(te_id, co_id)
            choice1 = input('Введите тип данных для обновления (title, description, teacher_id) or exit ')

    elif choice == '7':
        student_id = input('Введите id студента: ')
        delete_student(student_id)
    elif choice == '8':
        teacher_id = input('Введите id учителя: ')
        delete_student(teacher_id)
    elif choice == '9':
        cource_id = input('Введите id курса: ')
        delete_student(cource_id)
    
    elif choice =='10':
        department = input("Введите факультет: ")
        student = get_students_by_department(department)
    elif choice == '11':
        teacher_id = int(input("ID преподавателя: "))
        get_teacher_courses(teacher_id)
    elif choice == '12':
        student_id = int(input("ID студента: "))
        get_grades(student_id)

    elif choice == '13':
        student_id = int(input("ID студента: "))
        average_student(student_id)
    elif choice == '14':
        department = input("Название факультета: ")
        average_of_department(department)
# except:
        # print("ошибка! введи еще раз\n")

db_connection.close()
print("\nСоединение с базой данных закрыто.")
