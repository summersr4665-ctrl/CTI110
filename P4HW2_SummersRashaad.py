# Rashaad Summers
# 04/12/2026
# P4HW2
# The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

# Pseudocode / Algorithm
# 1. Create variables to store overtime total, regular pay total,
#    gross pay total, and employee count.
# 2. Ask the user to enter an employee name.
# 3. While the employee name is not "Done":
#    a. Ask for number of hours worked.
#    b. Ask for employee pay rate.
#    c. If hours worked is more than 40:
#         - Calculate overtime hours
#         - Calculate regular hours
#       Else:
#         - Overtime hours = 0
#         - Regular hours = hours worked
#    d. Calculate overtime pay, regular pay, and gross pay.
#    e. Display employee name and pay information.
#    f. Add overtime pay to overtime total.
#    g. Add regular pay to regular total.
#    h. Add gross pay to gross total.
#    i. Add 1 to employee count.
#    j. Ask for another employee name or "Done" to finish.
# 4. When the loop ends, display:
#    - total number of employees entered
#    - total overtime pay
#    - total regular pay
#    - total gross pay

overtime_total = 0
regular_total = 0
gross_total = 0
employee_count = 0

employee_name = input("Enter employee's name or \"Done\" to terminate: ")

while employee_name != "Done":
    hours_worked = float(input("How many hours did " + employee_name + " work? "))
    pay_rate = float(input("What is " + employee_name + "'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    print("---------------------------------------------")
    print("Employee name:  ", employee_name)
    print()
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}{regular_pay:<15.2f}{gross_pay:<.2f}")
    print()

    overtime_total = overtime_total + overtime_pay
    regular_total = regular_total + regular_pay
    gross_total = gross_total + gross_pay
    employee_count = employee_count + 1

    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

print()
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${overtime_total:.2f}")
print(f"Total amount paid for regular hours: ${regular_total:.2f}")
print(f"Total amount paid in gross: ${gross_total:.2f}")