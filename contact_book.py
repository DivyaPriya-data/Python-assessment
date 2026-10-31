menu = {}

while True:

    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")

    try:
        click = int(input("Select the operation (1,2,3,4): "))

        if click == 1:
            add_contact = input("Enter the contact name: ")
            add_number = input("Enter the phone number: ")

            menu[add_contact] = add_number

            print("Contact added successfully.")

        elif click == 2:
            print("Contacts:")

            for name, number in menu.items():
                print(name, ":", number)

        elif click == 3:
            search_name = input("Enter the name you want to search: ")

            if search_name in menu:
                print("Phone number:", menu[search_name])
            else:
                print("Contact not found.")

        elif click == 4:
            print("EXITED THE MENU")
            break

        else:
            print("Please select a valid option.")
    except ValueError :
        print("please enter valid input such as (1/2/3/4)")