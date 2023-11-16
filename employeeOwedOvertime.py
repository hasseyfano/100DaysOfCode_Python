# Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

# For this exercise, we need to determine whether or not the employee worked more than 40 hours this week. If they did, we need to pay them 110% of their hourly wage for any hours worked over the 40 hours.

# Because we have a condition to test here, a conditional statement is a good idea.

# Our first step though, is grabbing the values from the user. I'm going to grab the employee's name here, because I want to use it in the output. You can ignore this if you want to.

# For both the hours worked, and the hourly wage, I'm going to convert the user input to a floating point number. This is because we can reasonably expect the hourly wage to be something like 16.50, and for people to work fractions of an hour.

employee_name =input("Employee Name: ")
numberofHoursWorked=float(input("Number of Hours Worked: "))
hourlyWage=float(input("Hourly wage: "))
pay=(hourlyWage*numberofHoursWorked)
payWithovertimeWage=pay+(pay*1.1)

if numberofHoursWorked > 40:
    
    print(f"{employee_name} worked {numberofHoursWorked} hours last week and earned {payWithovertimeWage}")
else:
    print(f"{employee_name} worked {numberofHoursWorked} hours last week and earned {pay}")
    