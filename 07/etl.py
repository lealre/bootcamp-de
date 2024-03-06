from pathlib import Path
import csv

def read_csv(file_path: Path) -> list[dict]:
    """
    Reads a CSV file and returns a list of dictionaries representing each row.

    Args:
        file_path (Path): The path to the CSV file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary represents a row
                              from the CSV file, with keys as column names and values as
                              corresponding cell values.
    """

    rows_csv: list[dict] = []

    with open(file_path, 'r') as file:
        csv_data = csv.DictReader(file)

        for row in csv_data:
            rows_csv.append(row)
    
    return rows_csv

def process_data(dict_list: list[dict]) -> list[dict]:
    """
    Process a list of dictionaries containing 'Price' and 'Amount' information
    by calculating the total cost for each item and adding a 'Total' key to each dictionary.

    Args:
        dict_list (List[Dict[str, str]]): A list of dictionaries where each dictionary
            represents an item with 'Price' and 'Amount' keys.

    Returns:
        List[Dict[str, str]]: A modified list of dictionaries where each dictionary now
            contains an additional 'Total' key representing the calculated total cost
            (Price * Amount) for each item.
    """

    for dict_item in dict_list:
        dict_item['Total'] = int(dict_item['Price']) * int(dict_item['Amount'])
    
    return dict_list

def sales_per_category(dict_list: list[dict]) -> dict:
    """
    Calculate total sales per category from a list of dictionaries.

    Args:
        dict_list (List[Dict[str, Any]]): A list of dictionaries where each dictionary
            represents a sales item with 'Category' and 'Total' keys.

    Returns:
        Dict[str, int]: A dictionary where keys are unique categories and values are
            the total sales for each category.
    """
    sales_category: dict = {}

    for dict_item in dict_list:

        if dict_item['Category'] in sales_category.keys():
            sales_category[dict_item['Category']] += dict_item['Total']
        else:
            sales_category[dict_item['Category']] = dict_item['Total']
    
    return sales_category
