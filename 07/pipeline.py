from etl import read_csv, process_data, sales_per_category

csv_file = read_csv('07/sales.csv')
items = process_data(csv_file)
sales = sales_per_category(items)

print(sales)