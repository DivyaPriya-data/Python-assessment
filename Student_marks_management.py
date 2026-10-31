run_again = "yes"

while run_again == "yes":
    try:

        get_marks= int(input("enter the number of subjects: "))

        marks=[ ]

        for i in range(get_marks):
            mark=int(input(f"Enter the mark of subject {i+1} :"))
            marks.append(mark)

        length_of_marks = len(marks)  

        sum_of_the_marks = sum(marks) 

        avg=sum_of_the_marks/length_of_marks

        print("The marks are             :",marks)
        print("The average of your marks :",avg)

        if avg >= 80:
            print("your grade is 'A' ")
        elif avg >=60:
            print("your grade is 'B' ")
        elif avg >=40:
            print("your grade is 'C' ")
        else:
            print("you have failed - 'F' ")

    except ValueError:
        print("enter only valid numbers.")

    run_again = input("Do you want to find min,max and average for another list of values?(yes/no):").lower()

