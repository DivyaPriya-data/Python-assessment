run_again = "yes"

while run_again == "yes":
    try:
        user_input = input("enter the numbers to find min, max and average for :").split()

        user_input = [int(number) for number in user_input]
            
        len_of_user_input = len(user_input)
                
        sum_of_user_input = sum(user_input)
                
        avg = sum_of_user_input/len_of_user_input
            
    except ValueError:
        print("Please enter numbers only")
        continue 
    
    print("THE LIST :\n",user_input)
    print("The largest number from the list  :",max(user_input))
    print("The smallest number from the list :",min(user_input))
    print("The average of the number list    :",avg)

    run_again = input("Do you want to find min,max and average for another list of values?(yes/no):").lower()
