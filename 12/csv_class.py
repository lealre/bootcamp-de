import pandas as pd
from pathlib import Path
from typing import Any

class CsvProcessor:

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.df: pd.DataFrame = None
    
    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
    
    def filter_by(self, column: str, attribute: Any) -> pd.DataFrame:
        return self.df[self.df[column] == attribute]

if __name__ == '__main__':

    file_path: Path = '12/example.csv'

    csv_file = CsvProcessor(file_path= file_path)

    csv_file.load_csv()

    column = 'Year'
    attribute = 2022
    print(csv_file.filter_by(column= column, attribute= attribute))