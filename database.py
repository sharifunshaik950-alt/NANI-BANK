import psycopg2


def connect_database():
    connection = psycopg2.connect(
        host="localhost",
        database="NANI BANK",
        user="postgres",
        password="1234",
        port="5432"
    )
    return connection


def create_tables():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            account_number BIGINT PRIMARY KEY,
            customer_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20),
            address VARCHAR(200),
            balance NUMERIC(12,2) DEFAULT 0
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id SERIAL PRIMARY KEY,
            account_number BIGINT,
            transaction_type VARCHAR(20),
            amount NUMERIC(12,2),
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            balance_after NUMERIC(12,2),
            FOREIGN KEY (account_number)
            REFERENCES customers(account_number)
            ON DELETE CASCADE
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()

    print("Database tables are ready.")