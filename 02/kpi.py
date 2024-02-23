
# name
try:
    name = input('Name: ')
    if len(name) == 0:
        print('The name field is empty')
        exit()
except ValueError as e:
    print(e)


# salary
try:
    salary = input('Salary: ')
    salary = float(salary)
    if salary < 0:
        print('Number cannot be negative')
        exit()
except ValueError:
    print('Must be a number')
    exit()


# bonus
try:
    bonus = input('Bonus: ')
    bonus = float(bonus).as_integer_ratio
    if bonus < 0:
        print('Number cannot be negative')
        exit()
except ValueError:
    print('Must be a number')
    exit()

# kpi
bonus_value = 1000 + salary * bonus
print(f'Hello {name}! Your bonus value is {bonus_value}')