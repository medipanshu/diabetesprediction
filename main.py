from flask import Flask,render_template,request
import joblib

knn_model = joblib.load("D:/deepanshu/codes/Practice/diabetes/knn_model.pkl")
lr_model = joblib.load("D:/deepanshu/codes/Practice/diabetes/lr_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods = ['POST'])
def submit():
    if request.method == 'POST':
        age = int(request.form['age'])
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form["glucose"]) 
        blood_pressure = int(request.form['blood_pressure'])
        SkinThickness = int(request.form['SkinThickness'])
        insulin = int(request.form['insulin'])
        BMI = int(request.form['BMI']) 
        pedigree = int(request.form['pedigree'])
        model = request.form['model']
        print(request.form)
    yes = 'Chance of diabetes'
    no =  'No diabetes'
    if model == 'KNN':
        prediction = knn_model.predict([[pregnancies,glucose,blood_pressure,SkinThickness,insulin,BMI,pedigree,age]])
        if prediction[0] == 1: 
            return render_template('index.html',predict = yes)
        else:
            return render_template('index.html',predict = no)
    else:
        prediction = lr_model.predict([[pregnancies,glucose,blood_pressure,SkinThickness,insulin,BMI,pedigree,age]])
        if prediction[0] == 1:
            return render_template('index.html',predict = yes)
        else:
            return render_template('index.html',predict = no)
if __name__ == '__main__':
    app.run(debug=True)