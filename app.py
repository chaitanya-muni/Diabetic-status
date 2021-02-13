#Import Librarires
from flask import Flask, render_template,request
import pickle
import numpy as np


#load Model
model = pickle.load(open('Diabetic.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=[ 'POST'] )
def predict():
        if request.method == 'POST':
            Preg = int(request.form['Pregnancies'])
            glucose = int(request.form['Glucose'])
            BP = int(request.form['BloodPressure'])
            SKT = int(request.form['Skin Thickness'])
            Ins = int(request.form['Insulin'])
            BMI = float(request.form['BMI'])
            DPF = float(request.form['DiabetesPdigreeFunction'])
            Age = int(request.form['Age'])

            data = np.array([[Preg, glucose, BP, SKT, Ins, BMI, DPF, Age]])
            prediction = model.predict(data)
            if prediction <= 0:
                return render_template('home.html',predicted_texts = "Test Negative")
            else:
                return render_template('home.html', predicted_texts = "Test Positive")

        else:
            return render_template('home.html')       

if __name__=="__main__":
    app.run(debug = True)
