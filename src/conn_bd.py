# Импортируйте библиотеку psycopg2
import psycopg2
# Создайте подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="mydatabase",
    user="postgres",
    password="123"
)

# Данные для подключения к базе данных:
# Хост : sql_db
# Порт : 5432
# Имя базы данных : analysis
# Имя пользователя : simple
# Пароль : qweasd963

# Создайте подключение к базе данных
conn = psycopg2.connect(
    host="sql_db",
    port="5432",
    database="analysis",
    user="simple",
    password="qweasd963",
)