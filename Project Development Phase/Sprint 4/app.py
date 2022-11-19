import requests
import json
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY - "GAUNr8ZLGwNbm-g4suDTHyjmV4uRDdjuG0-xd0G_3eG2"
token_response = requests.post (https://iam.ng.bluemix.net/identitv/token', data-{"apikey": API_KEY, "grant_type":
mItoken = token_response. json() ["access_token"]
print ("mltoken", mItoken)
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mItoken}
# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_ scoring = {"input_data": ["fields": [array_of_input_fields],
"values": [array_of _values_to_be_scored, an
payload_scoring - {"input_data": [ ("field": [["GI",
"62
"G3*
"Creditscore"
"Gender"
"Age", "Tenure
"Balance"
"values": [[1, 0, 0, 68600,
1, 320000, 600000, 0,
20000, 1000000, 1000000, 1790932]131}
response_scoring - requests.post https://us-south.ml.cloud.ibm.com/ml/va/deployments/a0d8e0b0-f67e-4613-81f3-9b370a2c4459
print("Scoring response")
predictions = response_scoring.json()
print(predictions[ 'predictions '[el[ 'values '1[01[81)

from flask import render_template,Flask,request
import numpy as np
import pickle 
from sklearn.preprocessing import scale
app= Flask(__name__, template_folder='templates')

model = pickle.load(open("model.pkl",'rb'))



@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login.html')

@app.route('/home.html')
def home1():
    return render_template('home.html')
@app.route('/prediction.html')
def formpg():
    return render_template('prediction.html')

@app.route('/prediction.html',methods = ['POST'])
def predict():
    if request.method=='POST':
        name=request.form['Name']
        gender=request.form['gender']
        married=request.form['married']
        dependents=request.form['dependents']
        education=request.form['education']
        employed=request.form['employed']
        credit=request.form['credit']
        proparea=request.form['proparea']
        ApplicantIncome=float(request.form['ApplicantIncome'])
        CoapplicantIncome=float(request.form['CoapplicantIncome'])
        LoanAmount=float(request.form['LoanAmount'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
    if gender == 'Male':
        gender = 1
    else:
        gender = 0

    if married == 'Yes':
        married = 1
    else:
        married = 0

    if education == 'Graduate':
        education = 0
    else:
        education = 1

    if employed == 'Yes':
        employed = 1
    else:
        employed = 0

    if dependents == '3+':
        dependents = 3
    if credit == 'Yes':
        credit = 1
    else:
        credit = 0     
    if proparea == 'Urban':
        proparea = 2
    elif proparea == 'Rural':
        proparea = 0
    else:
        proparea = 1        
        

    

    features = [gender,married,dependents,education,employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,credit,proparea]
    
    con_features = [np.array(features)]
    


    prediction = model.predict(con_features)
    print(prediction)
    if prediction==1:
        return render_template('approve.html',prediction_text ='Congratulations! '+name+' You are eligible for loan')
    else:
        return render_template('reject.html',prediction_text ='Sorry '+name+' You are not eligible for loan')


if __name__ == "__main__":
    app.run(debug=True)