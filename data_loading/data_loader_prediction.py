import  pandas as pd
import os

class pred_loader:
    def __init__(self):
        self.dir='Output/Output.xlsx'
        self.path='Output/'
        self.dirs='Training_file/Input.xlsx'

    def data_load(self):
        try:
           data=pd.read_excel(self.dir)
           return data
        except Exception as e:
           raise e
    def processed_train_data_load(self):
        try:
           data=pd.read_excel(self.dirs)
           return data
        except Exception as e:
           raise e
