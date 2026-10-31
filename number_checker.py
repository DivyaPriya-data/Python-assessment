run_again = "yes"

while run_again == "yes":

    try:
        user_input = int(input("Enter the number you want to check: "))
    
        if user_input % 2 == 0:
            print(f"{user_input} is an Even number")
        else:
            print(f"{user_input} is an Odd number")

        if user_input > 0:
            print(f"{user_input} is a positive number")
        elif user_input < 0:
            print(f"{user_input} is a negative number")
        else:
            print("0 is neither positive nor negative")
        
    except ValueError:
        print("Please enter a valid number")
    
    run_again=input("Do you want to check another number(yes/no): ")