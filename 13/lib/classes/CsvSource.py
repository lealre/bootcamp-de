import os
import pandas as pd
from lib.classes.FileSource import FileSource

class CsvSource(FileSource):
 
    def create_path(self):
        ''' verify if there is a folder to specific extension '''
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, '13','data', 'source_csv')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
    
    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_file and file.endswith('.csv')]

        if new_files:
            print('New files detected:', new_files)
            # update previous files
            self.previous_file = current_files
        else:
            print('No CSV files detected!')
            self.get_data()
    
    def get_data(self):
        df_list: list = []
        for file in self.previous_file:
            try:
                path = f'{self.folder_path}/{file}'
                df = pd.read_csv(path)
                df_list.append(df)
            except Exception as e:
                print(e)