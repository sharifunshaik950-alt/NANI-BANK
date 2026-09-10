from database import create_tables

from account import create_account
from deposit import deposit
from withdraw import withdraw
from balance import check_balance
from statement import statement
from customer import search_customer, customers_list, all_customers_excel


def main():

    create_tables()

    current_account = None

    while True:

        print("\n")
        print("===================================")
        print("          NANI BANK")
        print("===================================")

        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Balance")
        print("6. Exit")
        print("7. Search Customer")
        print("8. Customers List")
        print("9. All Customers Excel")

        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            current_account = create_account()

        elif choice == "2":

            if current_account is None:

                print("Please create an account first.")

            else:

                deposit(current_account)

        elif choice == "3":

            if current_account is None:

                print("Please create an account first.")

            else:

                withdraw(current_account)

        elif choice == "4":

            if current_account is None:

                print("Please create an account first.")

            else:

                statement(current_account)

        elif choice == "5":

            if current_account is None:

                print("Please create an account first.")

            else:

                check_balance(current_account)

        elif choice == "6":

            print("Thank you for using NANI BANK.")
            break

        elif choice == "7":

            search_customer()

        elif choice == "8":

            customers_list()

        elif choice == "9":

            all_customers_excel()

        else:

            print("Invalid option!")


if __name__ == "__main__":
    main()