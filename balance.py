from database import connect_database


def check_balance(account_number):

    print("\n========== BALANCE ==========")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT customer_name, balance
        FROM customers
        WHERE account_number = %s
    """, (account_number,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None:

        print("Account not found.")
        return

    name = result[0]
    balance = result[1]

    print("Customer Name :", name)
    print("Account Number:", account_number)
    print("Current Balance:", balance)