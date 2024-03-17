import os
from lib.classes.AbstractDataSource import AsbtractDataSource

class FileSource(AsbtractDataSource):
    def __init__(self) -> None:
        self.previous_file: list = []
        self.start()
    
    def create_path(self):
        ''' verify if there is a folder to specific extension '''
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'extension_file')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
    
    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_file]

        if new_files:
            print('New files detected:', new_files)
            # update previous files
            self.previous_file = new_files
        else:
            print('No new files detected!')
        
    def get_data(self):
        pass
    
    def transform_data_to_df(self):
        pass
    
    def save_data(self):
        pass

    def show_files(self):
        print(self.previous_file)

    def start(self):
        return self.create_path()



# if __name__ == '__main__':


