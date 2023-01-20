import pandas as pd


class featurize:

    def change_dtype_to_datetime(self,data,column_list):
        for column_name in column_list:
             data[column_name]=pd.to_datetime(data[column_name])
        return data

    def separate_date_columns(self,data,column_name):
        data[column_name+"_day"]=data[column_name].dt.day
        data[column_name+"_month"]=data[column_name].dt.month
        data[column_name+"_year"]=data[column_name].dt.year
        data.drop(columns=column_name,axis=1,inplace=True)
        return data

    def separate_time_columns(self,data,col_list):
        for col in col_list:
            data[col+"_hour"]=data[col].dt.hour
            data[col+"_minute"]=data[col].dt.minute
        data.drop(columns=col_list, axis=1, inplace=True)
        return data



