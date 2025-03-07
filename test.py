employee_name = 'N/A'

def get_name():
    print(f'Employee name: {employee_name}')

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

