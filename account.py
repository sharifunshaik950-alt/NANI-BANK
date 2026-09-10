import random
from database import connect_database


def generate_account_number():

    while True:

        account_number = random.randint(1000000000, 9999999999)

        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT account_number FROM customers WHERE account_number = %s",
            (account_number,)
        )

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result is None:
            return account_number


def create_account():

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    while True:

        try:
            initial_amount = float(input("Enter initial deposit: "))

            if initial_amount < 0:
                print("Amount cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    account_number = generate_account_number()

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO customers
        (account_number, customer_name, phone, address, balance)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        account_number,
        name,
        phone,
        address,
        initial_amount
    ))

    if initial_amount > 0:

        cursor.execute("""
            INSERT INTO transactions
            (account_number, transaction_type, amount, balance_after)
            VALUES (%s, %s, %s, %s)
        """, (
            account_number,
            "DEPOSIT",
            initial_amount,
            initial_amount
        ))

    connection.commit()

    cursor.close()
    connection.close()

    print("\nAccount created successfully!")
    print("Customer Name :", name)
    print("Account Number:", account_number)
    print("Balance       :", initial_amount)

    return account_number