from Data_Featurization.featurization import featurize
from data_loading.data_loader import train_loader
from data_preprocessing.preprocessing import preprocessor
from feature_encoding.encoding import enocoder
from sklearn.model_selection import train_test_split
from data_modelling.modelling import model_selection
from file_operation.filemethod import file_op


class training_model:

    def __init__(self):
        self.load=train_loader()
        self.featurize=featurize()
        self.preprocessor=preprocessor()
        self.encode=enocoder()
        self.model=model_selection()
        self.file=file_op()

    def model_training(self):
        data=self.load.data_load()
        data=self.preprocessor.drop_null_values(data)
        column_list=['Date_of_Journey','Dep_Time','Arrival_Time']
        data=self.featurize.change_dtype_to_datetime(data,column_list)
        data=self.featurize.separate_date_columns(data,column_name='Date_of_Journey')
        data=self.featurize.separate_time_columns(data,col_list=['Dep_Time','Arrival_Time'])
        data=self.preprocessor.duration_column_processor(data,"Duration")
        data=self.preprocessor.drop_unneccessary_columns(data,col_list=['Additional_Info','Route','Date_of_Journey_year'])
        data=self.encode.one_hot(data,'Source')
        data=self.encode.mean_encoding(data,column=['Airline','Destination'])
        data=self.encode.manual_encoding(data,'Total_Stops')
        data=self.preprocessor.drop_unneccessary_columns(data,col_list=['Source','Duration'])
        x = data.drop(columns=['Price'], axis=1)
        y = data['Price']
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=36, test_size=1 / 3)
        model_name, model = self.model.best_model(x_train=x_train, x_test=x_test, y_train=y_train, y_test=y_test)
        self.file.model_saving(model_name, model)
        return model_name


if __name__=="__main__":
    train=training_model()
    train.model_training()
