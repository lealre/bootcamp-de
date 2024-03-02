import pandas as pd
from pathlib import Path
import glob
import os

def extract_data(file_path: str) -> pd.DataFrame:
    '''
     Extract data from JSON files in the specified directory.

    Parameters:
    -----------
    file_path : str
        The path to the directory containing JSON files.

    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame containing the concatenated data from all JSON files.
    '''
     
    json_files = glob.glob(os.path.join(file_path, '*.json'))
    df_list = [pd.read_json(file) for file in json_files]
    df = pd.concat(df_list, ignore_index= True)

    return df


def calculate_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Calculate the total sales by multiplying the 'Price' and 'Amount' columns.

    Parameters:
    -----------
    df : pd.DataFrame
        The input DataFrame containing the 'Price' and 'Amount' columns.

    Returns:
    --------
    pd.DataFrame
        A new DataFrame with an additional 'Total' column representing the calculated total sales.
    '''

    df['Total'] = df['Price'] * df['Amount']

    return df


def load_data(df: pd.DataFrame, output_format: list) -> None:
    '''
    Save the DataFrame to specified output formats.

    Parameters:
    -----------
    df : pd.DataFrame
        The input DataFrame to be saved.

    output_format : list
        A list containing the desired output formats. Supported formats: ['csv', 'parquet'].
    '''

    if 'csv' in output_format:
        df.to_csv('08/output.csv')
    if 'parquet' in output_format:
        df.to_parquet('08/output.parquet')


def pipeline_calculate_total_sales_consolidated(path_folder: Path, output_format: list) -> None:
    '''
    Perform a data pipeline to calculate total sales from JSON files and save the result.

    Parameters:
    -----------
    path_folder : Path
        The path to the folder containing JSON files.

    output_format : list
        A list containing the desired output formats. Supported formats: ['csv', 'parquet'].
    '''
    
    df = extract_data(file_path=path_folder)
    df = calculate_total_sales(df=df)
    load_data(df=df, output_format=output_format)


if __name__ == '__main__':

    folder: Path = '08/data'
    output_format: list = ['csv', 'parquet']
    pipeline_calculate_total_sales_consolidated(path_folder=folder,output_format=output_format)