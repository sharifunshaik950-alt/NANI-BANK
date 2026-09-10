from database import connect_database


def deposit(account_number):

    print("\n========== DEPOSIT ==========")

    while True:

        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid amount.")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT balance
        FROM customers
        WHERE account_number = %s
    """, (account_number,))

    result = cursor.fetchone()

    if result is None:

        print("Account not found.")

        cursor.close()
        connection.close()
        return

    old_balance = float(result[0])
    new_balance = old_balance + amount

    cursor.execute("""
        UPDATE customers
        SET balance = %s
        WHERE account_number = %s
    """, (
        new_balance,
        account_number
    ))

    cursor.execute("""
        INSERT INTO transactions
        (account_number, transaction_type, amount, balance_after)
        VALUES (%s, %s, %s, %s)
    """, (
        account_number,
        "DEPOSIT",
        amount,
        new_balance
    ))

    connection.commit()

    cursor.close()
    connection.close()

    print("\nDeposit successful!")
    print("Account Number :", account_number)
    print("Deposited Amount:", amount)
    print("New Balance    :", new_balance)