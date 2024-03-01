import pandas as pd
import glob
import os

# func to extract
folder = '08/data'
def extract_data(file_path):
    json_files = glob.glob(os.path.join(file_path, '*.json'))
    df_list = [pd.read_json(file) for file in json_files]
    df = pd.concat(df_list, ignore_index= True)
    return df
# func to tranform

# func to load

if __name__ == '__main__':
    print(extract_data(folder))
