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
    host="sql_db",
    port="5432",
    database="analysis",
    user="simple",
    password="qweasd963",
)
# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("create schema if not exists itresume15608;")
cur.execute("DROP TABLE IF EXISTS itresume15608.orders")
cur.execute("DROP TABLE IF EXISTS itresume15608.customers")
cur.execute("DROP TABLE IF EXISTS itresume15608.employees")

# Ниже напишите код запросов для создания таблиц
cur.execute("CREATE TABLE itresume15608.customers("
            "customer_id varchar(5) PRIMARY KEY,"
            "company_name varchar(100) NOT NULL,"
            "contact_name varchar(100) NOT NULL)"
            )
cur.execute("CREATE TABLE itresume15608.employees("
            "employee_id SERIAL PRIMARY KEY,"
            "first_name varchar(25) NOT NULL,"
            "last_name varchar(35) NOT NULL,"
            "title varchar(100) NOT NULL,"
            "birth_date date NOT NULL,"
            "notes text)"
            )
cur.execute("CREATE TABLE itresume15608.orders("
            "order_id int PRIMARY KEY,"
            "customer_id VARCHAR(5) REFERENCES itresume15608.customers(customer_id) NOT NULL,"
            "employee_id INTEGER REFERENCES itresume15608.employees(employee_id) NOT NULL,"
            "order_date date NOT NULL,"
            "ship_city varchar(100) NOT NULL)"
            )

# Зафиксируйте изменения в базе данных
conn.commit()

# Теперь приступаем к операциям вставок данных
# Запустите цикл по списку customers_data и выполните запрос формата
# "INSERT INTO itresume3270.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning
for row in customers_data:
    query = f"INSERT INTO itresume15608.customers (customer_id, company_name, contact_name) VALUES ({', '.join(['%s'] * len(row))}) returning *"
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_customers = cur.fetchall()

# Запустите цикл по списку employees_data и выполните запрос формата
# "INSERT INTO itresume15608.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
for row in employees_data:
    query = f"INSERT INTO itresume15608.employees (first_name, last_name, title, birth_date, notes) VALUES ({', '.join(['%s'] * len(row))}) returning *"
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_employees = cur.fetchall()

# Запустите цикл по списку orders_data и выполните запрос формата
# "INSERT INTO itresume15608.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
for row in orders_data:
    query = f"INSERT INTO itresume15608.orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES ({', '.join(['%s'] * len(row))}) returning *"
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()
