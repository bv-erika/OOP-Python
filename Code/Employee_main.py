from Employee import Employee

employeeList = []

execution = True
while execution:
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    operation = int(input(
        "Enter an operation \n"
        "1.Add Employee \n"
        "2.Get Employees \n"
        "3.Average Salary \n"
        "4.Who has most emails \n"
        "5.Who earns more \n"
        "6.Exit \n"))
    if operation == 1:
        name = input("Enter a name: ")
        salary = int(input("Enter the salary: "))
        birthday = input("Enter the birthday as DD.MM.YYYY: ")
        email = input("Give an email: ")
        position = input("Give a position(Lecturer,Prof,Dr): ")
        employee = Employee(name, salary, birthday, email,position)
        employeeList.append(employee)

    elif operation == 2:
        if len(employeeList) == 0:
            print("No available employee yet!")
            continue
        for employee in employeeList:
            employee.print()
        operation2 = int(input("Enter an operation \n 1.Add email to employee \n 2.Increase Salary \n 3.Exit \n"))
        if operation2 == 1:
            chooseUser = input("Enter the name of the employee to add email: ")
            addingEmail = input("Enter the email address to add: ")
            for employee in employeeList:
                if employee.name == chooseUser:
                    employee.emailList.append(addingEmail)
            print("Added!")
        elif operation2 == 2:
            chooseUser = input("Enter the name of the employee to increase the salary: ")
            for employee in employeeList:
                if employee.name == chooseUser:
                    employee.increaseBy10()
            print("Increased!")
        elif operation2 == 3:
            continue
        else:
            print("Wrong input!")
    elif operation == 3:
        if len(employeeList) == 0:
            print("No available employee yet!")
            continue
        total = 0
        employeeCount = 0
        for employee in employeeList:
            total += employee.salary
            employeeCount += 1
        print("Average Salary is:", total / employeeCount)
    elif operation == 4:
        if len(employeeList) == 0:
            print("No available employee yet!")
            continue
        mostEmails = 0
        mostEmailEmp = employeeList[0]
        for employee in employeeList:
            if len(employee.emailList) > mostEmails:
                mostEmailEmp = employee
        print(mostEmailEmp.getName(), "has the most emails with ", len(mostEmailEmp.getEmailList()))
    elif operation == 5:
        if len(employeeList) == 0:
            print("No available employee yet!")
            continue
        maxSalary = 0
        maxSalariedEmployee = employeeList[0]
        for employee in employeeList:
            if employee.getSalary() > maxSalary:
                maxSalary = employee.getSalary()
                maxSalariedEmployee = employee
        print("Max salaried employee is:", maxSalariedEmployee.getName())
        print("The salary is:", maxSalariedEmployee.getSalary())

    elif operation == 6:
        execution = False
    else:
        print("Wrong input!")
