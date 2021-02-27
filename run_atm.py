from cli import ATM
from cli.exceptions import InvalidSelection

if __name__ == "__main__":
    atm = ATM()

    while True:
        atm.menu()

        choice = input("Choose action >>>> ")

        try:
            choice = int(choice)

            if atm.quit == choice:
                break
            atm.choice(choice)
        except (ValueError, InvalidSelection):
            print("Invalid selection, please try again...\n\n\n")
