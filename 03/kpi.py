
#name
validate_name = True

while validate_name:
    try:
        name = input('Name: ')
        if len(name) == 0:
            print('The name field is empty.')
        elif any(char.isdigit() for char in name):
            print('Name cannot contain numbers.')
        else:
            validate_name = False
    except ValueError as e:
        print(e)


# salary
validate_salary = True

while validate_salary:
    try:
        salary = input('Salary: ')
        salary = float(salary)
        if salary < 0:
            print('Number cannot be negative')
        else:
            validate_salary = False
    except ValueError:
        print('Must be a number')

# bonus
validate_bonus = True

while validate_bonus:
    try:
        bonus = input('Bonus: ')
        bonus = float(bonus)
        if bonus < 0:
            print('Number cannot be negative')
        else:
            validate_bonus = False
    except ValueError:
        print('Must be a number')

# kpi
bonus_value = 1000 + salary * bonus
print(f'Hello {name}! Your bonus value is {bonus_value}')