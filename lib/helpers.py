from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input('Enter the employees name: ')
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print('not found')



def find_employee_by_id():
    id = input('Enter employee id: ')
    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print('not found')


def create_employee():
    name = input('Enter name: ')
    job_title = input('Enter job title: ')
    department_id = input('Enter department id: ')
    try:
        department_id = int(department_id)
        employee = Employee.create(name, job_title, department_id)
        print(f'success: {employee} created')
    except Exception as exc:
        print('error ', exc )


def update_employee():
    id_ = input('Enter employee id: ')
    if employee := Employee.find_by_id(id_):
        try:
            name = input('Enter updated name: ')
            employee.name = name
            job_title = input('Enter updated job title: ')
            employee.job_title =job_title
            department_id = input('Enter updated department id: ')
            employee.department_id = int(department_id)
            employee.update()
            print(f'success {employee} updated')

        except Exception as exc:
            print('did not find', exc)
    else:
        print('id not found')


def delete_employee():
    id_= input('Enter employee id: ')
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'{employee} was deleted')
    else:
        print('error')


def list_department_employees():
    department_id = input('Enter department id: ')
    department = Department.find_by_id(department_id)
    if department:
        print(f'department was found', department)
        department_employees = department.employees()
        for employee in department_employees:
            print(f'{employee.name}\n {employee.job_title}')
    else:
        print('department not found')
    
    