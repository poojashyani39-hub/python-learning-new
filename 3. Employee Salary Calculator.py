def calculate_salary():
    try:
        enter_salary=float(input("Enter your salary: ")) #take input from user

        if enter_salary < 0:    #if salary is negative, print error message and return
            print("Salary cannot be negative. Please enter a valid salary.")
            return
        
        hra=enter_salary * 0.20  #calculate HRA(House Rent Allowance.)
        da= enter_salary * 0.10  #calculate DA(Dearness Allowance.)
        pf= enter_salary * 0.12  #calculate PF(Provident Fund.)

        gross_salary= enter_salary + hra + da   

        net_salary = gross_salary - pf

        #print salary details

        print("\n Salary Details:")   

        print("basic salary:", enter_salary)
        print("HRA (20%):", hra)
        print("DA (10%):", da)
        print("PF (12%):", pf)
        print("Gross salry:", gross_salary)
        print("Net salary:", net_salary)

    except ValueError:
        print("Invalid input. Please enter a numeric value for salary.")  #if user enters a non-numeric value, print error message

calculate_salary()  #call the function to execute the salary calculation