def main():
    # Исходные данные для заполнения таблиц
    import csv

    with open('customers_data.csv', newline='') as file:
        customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

    with open('employees_data.csv', newline='') as file:
        employees_data = [row for row in csv.reader(file) if 'first_name' not in row]

    with open('orders_data.csv', newline='') as file:
        orders_data = [row for row in csv.reader(file) if 'order_id' not in row]

    # Импортируйте библиотеку psycopg2
    import psycopg2
    # Создайте подключение к базе данных
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="postgres",
        password="123"
    )
    # Открытие курсора
    cur = conn.cursor()

    # Не меняйте и не удаляйте эти строки - они нужны для проверки
    cur.execute("create schema if not exists itresume15608;")
    cur.execute("DROP TABLE IF EXISTS itresume15608.orders")
    cur.execute("DROP TABLE IF EXISTS itresume15608.customers")
    cur.execute("DROP TABLE IF EXISTS itresume15608.employees")

    # Ниже напишите код запросов для создания таблиц
    cur.execute("CREATE TABLE customer("
                "customer_id varchar(5) PRIMARY KEY,"
                "company_name varchar(100) PRIMARY KEY,"
                "contact_name varchar(100) PRIMARY KEY)")
    cur.execute("CREATE TABLE employees("
                "employee_id int PRIMARY KEY,"
                "first_name varchar(25) PRIMARY KEY,"
                "last_name varchar(35) PRIMARY KEY,"
                "title varchar(100) PRIMARY KEY,"
                "birth_date date PRIMARY KEY,"
                "notes text)")
    cur.execute("CREATE TABLE orders("
                "order_id int PRIMARY KEY,"
                "customer_id REFERENCES customer(customer_id) NOT NULL,"
                "employee_id REFERENCES employees(employee_id) NOT NULL,"
                "order_date date PRIMARY KEY,"
                "ship_city varchar(100) PRIMARY KEY)")

    # Зафиксируйте изменения в базе данных
    conn.commit()

    # Теперь приступаем к операциям вставок данных
    # Запустите цикл по списку customers_data и выполните запрос формата
    # INSERT INTO itresume3270.table (column1, column2, ...) VALUES (%s, %s, ...) returning ", data)
    # В конце каждого INSERT-запроса обязательно должен быть оператор returning

    for ...

    # Не меняйте и не удаляйте эти строки - они нужны для проверки
    conn.commit()
    res_customers = cur.fetchall()

    # Запустите цикл по списку employees_data и выполните запрос формата
    # INSERT INTO itresume15608.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
    # В конце каждого INSERT-запроса обязательно должен быть оператор returning *
    for ...

    # Не меняйте и не удаляйте эти строки - они нужны для проверки
    conn.commit()
    res_employees = cur.fetchall()

    # Запустите цикл по списку orders_data и выполните запрос формата
    # INSERT INTO itresume15608.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
    # В конце каждого INSERT-запроса обязательно должен быть оператор returning *
    for ...

    # Не меняйте и не удаляйте эти строки - они нужны для проверки
    conn.commit()
    res_orders = cur.fetchall()

    # Закрытие курсора
    cur.close()

    # Закрытие соединения
    conn.close()

if __name__ == '__main__':
    main('PyCharm')

