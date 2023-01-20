import  pandas as pd


class train_loader:
    def __init__(self):
        self.dir='Training_file/Data_Train.xlsx'

    def data_load(self):
        try:
           data=pd.read_excel(self.dir)
           return data
        except Exception as e:
           raise e
