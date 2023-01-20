import pandas as pd

class enocoder:

    def one_hot(self,data,column):
        for city in data[column].unique():
            data[column+"_"+city]=data[column].apply(lambda x:1 if x==city else 0)
        return data

    def mean_encoding(self,data,column):
        for col in column:
            values=data.groupby([col])['Price'].mean().sort_values().index
            dictionary={key:value for value,key in enumerate(values)}
            data[col]=data[col].map(dictionary)
        return data

    def dict_value(self,train_data,pred_data,column):
        values=train_data.groupby([column])['Price'].mean().sort_values().index
        dictionary={key:value for value,key in enumerate(values)}
        pred_data.replace(list(pred_data[column])[0],dictionary[list(pred_data[column])[0]],inplace=True)
        return pred_data

    def dict_data(self,train_data,column):
        values=train_data.groupby([column])['Price'].mean().sort_values().index
        dictionary={key:value for value,key in enumerate(values)}
        return dictionary

    def source_column_addition(self,train_data,pred_data):
        column=train_data.drop(columns='Price',axis=1)
        for col in list(column.columns):
            if col not in list(pred_data.columns):
                pred_data[col]=0
        return pred_data



    def manual_encoding(self,data,column):
        stops={'non-stop':0, '2 stops':2, '1 stop':1, '3 stops':3, '4 stops':4}
        data[column]=data[column].map(stops)
        return data