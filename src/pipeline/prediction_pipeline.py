import sys
import os
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 gender:str,
                 SeniorCitizen:int,
                 Partner:str,
                 Dependents:str,
                 tenure:int,
                 PhoneService:str,
                 MultipleLines:str,
                 InternetService:str,
                 OnlineSecurity:str,
                 OnlineBackup:str,
                 DeviceProtection:str,
                 TechSupport:str,
                 StreamingTV:str,
                 StreamingMovies:str,
                 Contract:str,
                 PaperlessBilling:str,
                 PaymentMethod:str,
                 MonthlyCharges:int,
                 TotalCharges:int
                 ):
        
        self.gender=gender
        self.SeniorCitizen=SeniorCitizen
        self.Partner=Partner
        self.Dependents=Dependents	
        self.tenure=tenure
        self.PhoneService=PhoneService
        self.MultipleLines=MultipleLines
        self.InternetService=InternetService
        self.OnlineSecurity=OnlineSecurity
        self.OnlineBackup=OnlineBackup
        self.DeviceProtection=DeviceProtection
        self.TechSupport=TechSupport
        self.StreamingTV=StreamingTV	
        self.StreamingMovies=StreamingMovies
        self.Contract=Contract
        self.PaperlessBilling=PaperlessBilling
        self.PaymentMethod=PaymentMethod
        self.MonthlyCharges=MonthlyCharges
        self.TotalCharges=TotalCharges
        
        
        
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'gender':[self.gender],
                'SeniorCitizen':[self.SeniorCitizen],
                'Partner':[self.Partner],
                'Dependents':[self.Dependents],
                'tenure':[self.tenure],
                'PhoneService':[self.PhoneService],
                'MultipleLines':[self.MultipleLines],
                'InternetService':[self.InternetService],
                'OnlineSecurity':[self.OnlineSecurity],
                'OnlineBackup':[self.OnlineBackup],
                'DeviceProtection':[self.DeviceProtection],
                'TechSupport':[self.TechSupport],
                'StreamingTV':[self.StreamingTV],
                'StreamingMovies':[self.StreamingMovies],
                'Contract':[self.Contract],
                'PaperlessBilling':[self.PaperlessBilling],
                'PaymentMethod':[self.PaymentMethod],
                'MonthlyCharges':[self.MonthlyCharges],
                'TotalCharges':[self.TotalCharges]
                
            }
            df = pd.DataFrame(custom_data_input_dict)
            
            logging.info('Dataframe Gathered')
            logging.info(f'new Dataframe   : \n{df.to_string()}')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)