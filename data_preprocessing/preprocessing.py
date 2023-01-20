import pandas as pd


class preprocessor:

    def drop_null_values(self,data):
        data.dropna(inplace=True)
        return data


    def prepocess_duration(self,x):
        if 'h' not in x:
            x='0h '+x
        elif 'm' not in x:
            x=x+' 0h'
        return x

    def duration_column_processor(self,data,col_name):
        data[col_name]=data[col_name].apply(self.prepocess_duration)
        data['duration_hours']=data[col_name].apply(lambda x:int(x.split(' ')[0][0:-1]))
        data['duration_minutes'] = data[col_name].apply(lambda x: int(x.split(' ')[1][0:-1]))
        return data


    def drop_unneccessary_columns(self,data,col_list):
        data.drop(columns=col_list,axis=1,inplace=True)
        return data









