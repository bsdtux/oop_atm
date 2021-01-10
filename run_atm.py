from atm import ATM, InvalidChoice


if __name__ == '__main__':
    atm = ATM()

    while True:
        atm.menu()

        choice = input("Choose action >>>> ")

        try:
            choice = int(choice)

            if choice == 6:
                break
            atm.choice(choice)
        except (ValueError, InvalidChoice):
            print('Invalid selection, please try again...\n\n\n')

       
