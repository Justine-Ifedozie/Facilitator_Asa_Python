from employeepayrollfunction import add_employee_payroll, federal_witholding, state_witholding, total_deduction, net_pay

payroll = []
accounts = []

meNU = True
while meNU:

        mainMenu = """
Welcome to Semicolon Employees Payroll!
=============================
List of payroll functions:

Press: 
1. Add Employee Payroll
2. View Employees Payroll
3. Update Employees Payroll
4. Exit
=============================
        """

        print(mainMenu)
        menu = int(input("Press a number to make a selection between 1 - 4: "))

        if menu < 0 or menu > 4:
                print("You entered an invalid option!! Kindly try again or press 0 for Yoruba")
                menu = int(input("Press a number to make a selection between 1 - 4: "))


        match menu:
                case 1:
                        employeeName = input("Enter Employee Name: ")
                        numberOfHoursWorked = int(input("Enter number of hours worked in a week: "))
                        hourlyPayrate = float(input("Enter hourly payrate: "))
                        federalTaxRate = float(input("Enter Federal tax witholding rate: "))
                        stateTaxRate = float(input("Enter State tax witholding rate: "))

                        gross_pay = add_employee_payroll(numberOfHoursWorked, hourlyPayrate)
                        
                        federal = federal_witholding(gross_pay, federalTaxRate)
                        state = state_witholding(gross_pay, stateTaxRate)

                        total = total_deduction(federal, state)
                        net = net_pay(gross_pay, total)

                        payroll.append(f'Employee name: {employeeName}')
                        payroll.append(f'Hours Worked: {numberOfHoursWorked}')
                        payroll.append(f'Pay Rate: {hourlyPayrate}')
                        payroll.append(f'Gross Pay: {gross_pay}')
                        payroll.append(f'Deductions: Federal Witholding(20%) - {federal}. State Witholding(9.0%) - {state}. Total Deductions - {total}')
                        payroll.append(f'Net Pay: {net} ')

                        accounts.append(payroll)
                case 2:
                        for index in range(len(accounts)):
                                accounts[index]
                        print(accounts)

                case 3:

                        print("Update Employees payroll")

                case 4:
                        meNU = False
