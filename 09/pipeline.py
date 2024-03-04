from etl import pipeline_calculate_total_sales_consolidated
from pathlib import Path

folder: Path = '08/data'
output_format: list = ['csv', 'parquet']

pipeline_calculate_total_sales_consolidated(path_folder=folder,output_format=output_format)