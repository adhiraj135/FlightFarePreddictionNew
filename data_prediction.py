from Data_Featurization.featurization import featurize
from data_loading.data_loader_prediction import pred_loader
from data_preprocessing.preprocessing import preprocessor
from feature_encoding.encoding import enocoder
from data_loading.data_loader import train_loader



class prediction_model:

    def __init__(self):
        self.load=pred_loader()
        self.featurize=featurize()
        self.preprocessor=preprocessor()
        self.encode=enocoder()
        self.train_load=train_loader()



    def model_prediction(self):
        data=self.load.data_load()
        data=self.preprocessor.drop_null_values(data)
        column_list=['Date_of_Journey','Dep_Time','Arrival_Time']
        data=self.featurize.change_dtype_to_datetime(data,column_list)
        data=self.featurize.separate_date_columns(data,column_name='Date_of_Journey')
        data=self.featurize.separate_time_columns(data,col_list=['Dep_Time','Arrival_Time'])
        data=self.preprocessor.duration_column_processor(data,"Duration")
        data=self.preprocessor.drop_unneccessary_columns(data,col_list=['Additional_Info','Route','Date_of_Journey_year'])
        print(data.values)
        df=self.train_load.data_load()
        dic=self.encode.dict_data(train_data=df,column='Airline')
        print(dic)
        dic1= self.encode.dict_data(train_data=df, column='Destination')
        print(dic1)
        data=self.encode.dict_value(train_data=df,pred_data=data,column='Airline')
        data=self.encode.dict_value(train_data=df, pred_data=data, column='Destination')
        data=self.encode.manual_encoding(data,'Total_Stops')
        final_train_data=self.load.processed_train_data_load()
        data=self.encode.source_column_addition(train_data=final_train_data,pred_data=data)
        self.encode.one_hot(data,'Source')
        data = self.preprocessor.drop_unneccessary_columns(data, col_list=['Source', 'Duration'])
        print(data.columns)
        return data


if __name__=="__main__":
    pred=prediction_model()
    pred.model_prediction()

