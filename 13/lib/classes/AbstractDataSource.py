from abc import ABC, abstractmethod

class AsbtractDataSource(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError('Method not implemented!')
    
    @abstractmethod
    def get_data(self):
        raise NotImplementedError('Method not implemented!')
    
    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError('Method not implemented!')
    
    @abstractmethod
    def save_data(self):
        raise NotImplementedError('Method not implemented!')
    
    def hello_world():
        print('Hello World!')
    
    