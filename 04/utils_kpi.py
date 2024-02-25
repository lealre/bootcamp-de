
def calculate_and_display_kpi(name: str, salary: float, bonus: float) -> None:
    """
    Calculate and display the KPI (Key Performance Indicator) for an individual.

    Parameters:
    -----------
    name : str
        The name of the individual.

    salary : float
        The salary of the individual.

    bonus : float
        The bonus rate for the individual.
    """ 

    bonus_value = 1000 + salary * bonus

    print(f'Hello {name}! Your bonus value is {bonus_value}')

def validate_name_field() -> str: 
    """
    Validate and retrieve a non-empty name input from the user.

    Returns:
    --------
    str
        The validated name input.
    """

    validate_name = True

    while validate_name:
        try:
            input_name = input('Name: ')
            if len(input_name) == 0:
                print('The name field is empty.')
            elif any(char.isdigit() for char in input_name):
                print('Name cannot contain numbers.')
            else:
                validate_name = False
        except ValueError as e:
            print(e)
    
    return input_name


def validate_salary_field() -> float:
    """
    Validate and retrieve a non-negative salary input from the user.

    Returns:
    --------
    float
        The validated salary input.
    """

    validate_salary = True

    while validate_salary:
        try:
            input_salary = input('Salary: ')
            input_salary = float(input_salary)
            if input_salary < 0:
                print('Number cannot be negative')
            else:
                validate_salary = False
        except ValueError:
            print('Must be a number')
        
    return input_salary

def validate_bonus_field() -> float:
    """
    Validate and retrieve a non-negative bonus input from the user.

    Returns:
    --------
    float
        The validated bonus input.
    """

    validate_bonus = True

    while validate_bonus:
        try:
            input_bonus = input('Bonus: ')
            input_bonus = float(input_bonus)
            if input_bonus < 0:
                print('Number cannot be negative')
            else:
                validate_bonus = False
        except ValueError:
            print('Must be a number')
    
    return input_bonus

