from database import connect_database


def withdraw(account_number):

    print("\n========== WITHDRAW ==========")

    while True:

        try:
            amount = float(input("Enter withdrawal amount: "))

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

    if amount > old_balance:

        print("Insufficient balance.")

        cursor.close()
        connection.close()
        return

    new_balance = old_balance - amount

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
        "WITHDRAW",
        amount,
        new_balance
    ))

    connection.commit()

    cursor.close()
    connection.close()

    print("\nWithdrawal successful!")
    print("Account Number :", account_number)
    print("Withdrawn Amount:", amount)
    print("New Balance    :", new_balance)