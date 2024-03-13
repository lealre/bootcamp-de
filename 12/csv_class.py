import pandas as pd
from pathlib import Path
from typing import Any

class CsvProcessor:

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.df: pd.DataFrame = None
    
    def load_csv(self):
        '''
        Loads the CSV file specified in the file_path attribute into a pandas DataFrame.
        '''
        self.df = pd.read_csv(self.file_path)
    
    def filter_by(self, column: str, attribute: Any) -> pd.DataFrame:
        '''
        Filters the DataFrame by the given column and attribute.

        Args:
            column (str): The column name to filter by.
            attribute (Any): The value to filter for in the specified column.

        Returns:
            pd.DataFrame: The filtered DataFrame containing only the rows where the specified column matches the given attribute.
        '''
        return self.df[self.df[column] == attribute]

if __name__ == '__main__':

    file_path: Path = '12/example.csv'

    csv_file = CsvProcessor(file_path= file_path)

    csv_file.load_csv()

    column = 'Year'
    attribute = 2022
    print(csv_file.filter_by(column= column, attribute= attribute))