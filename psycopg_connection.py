import psycopg2

conn = psycopg2.connect("dbname=cursos_mvcad user=postgres password=123456 host=localhost")

conn.autocommit = True

cursor = conn.cursor()

