

hr_list = [
    ('0123','HR', 'Rebecca Yang', '69000'),
    ('0121', 'IT', 'Mark Blick', '67000'),
    ('0068', 'IT', 'Kahana Larsen', '112000'),
    ('0234', 'OPS', 'Jim Smith', '54000')]


#Update Marks last name to blicky-hawley

for i in range(len(hr_list)):
    if hr_list[i][2] == 'Mark Blick':
        hr_list[1] = (hr_list[i][0], hr_list[i][1], 'Mark Blick_Hawley', hr_list[i][3])
    elif hr_list[i][2] == 'Jim Smith':
        hr_list[i] = (hr_list[i][0], 'CS', 'Jim Smith', '60000')


#Display Update
print("Employee#  | DeptCode   | Name                 | Salary")
print("--------------------------------------------------")
for emp in hr_list:
    employee_number, dept_code, name, salary = emp
    formatted_salary = f"{int(salary):,}"
    print(f"{employee_number}        |  {dept_code}      | {name:<20} | {formatted_salary}")