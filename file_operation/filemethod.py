import os
import pickle


class file_op:

    def __init__(self):
        self.dir='model/'

    def model_saving(self,model_name,model):
        try:
           path=os.path.join(self.dir,model_name)
           if not os.path.isdir(path):
              os.makedirs(path,exist_ok=True)

           with open(self.dir+model_name+"/"+model_name+'.sav','wb') as f:
              pickle.dump(model,f)
        except Exception as e:
            raise e
    def model_loading(self,model_name):
        try:
            with open(self.dir+model_name+"/"+model_name+".sav",'rb') as f:
               return pickle.load(f)
        except Exception as e:
            raise e

    def model_finder(self):
        try:
            for model in os.listdir(self.dir):
                return model
        except Exception as e:
            raise e
