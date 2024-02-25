from utils_kpi import validate_name_field, validate_salary_field, validate_bonus_field, calculate_and_display_kpi

name = validate_name_field()

salary = validate_salary_field()

bonus = validate_bonus_field()

calculate_and_display_kpi(name, salary, bonus)
