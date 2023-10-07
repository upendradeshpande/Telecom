from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        data=CustomData(
            gender=str(request.form.get('gender')),
            SeniorCitizen=int(request.form.get('SeniorCitizen')),
            Partner=str(request.form.get('Partner')),
            Dependents=str(request.form.get('Dependents')),
            tenure=int(request.form.get('tenure')),
            PhoneService=str(request.form.get('PhoneService')),
            MultipleLines=str(request.form.get('MultipleLines')),
            InternetService=str(request.form.get('InternetService')),
            OnlineSecurity=str(request.form.get('OnlineSecurity')),
            OnlineBackup=str(request.form.get('OnlineBackup')),
            DeviceProtection=str(request.form.get('DeviceProtection')),
            TechSupport=str(request.form.get('TechSupport')),
            StreamingTV=str(request.form.get('StreamingTV')),
            StreamingMovies=str(request.form.get('StreamingMovies')),
            Contract=str(request.form.get('Contract')),
            PaperlessBilling=str(request.form.get('PaperlessBilling')),
            PaymentMethod=str(request.form.get('PaymentMethod')),
            MonthlyCharges=int(request.form.get('MonthlyCharges')),
            TotalCharges=int(request.form.get('TotalCharges'))
            
    
            
           
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        def final_result(pred):
            if pred==1:
                result='customer is churning telcos service'
            else:
                result = 'customer not churning telcos service very much'
            return result
        
        final_results = final_result(pred)
            

        return render_template('results.html',final_results = final_result(pred))




if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
    #app.run(host='0.0.0.0',port=5080)

