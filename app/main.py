import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="195.80.51.6",
        database="потом решим",
        user="postgres",
        password="123",
        port="5432"
    )
    return conn