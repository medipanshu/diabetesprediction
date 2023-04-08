### Diabetes Prediction

Machine learning model that predicts whether a person is diabetic based on various features(['Age','Pregnancies','BMI','Insulin','BloodPressure','Glucose','SkinThickness','DiabetesPedigreeFunction']).

The site will take some time as it is hosted on a free cloud service provider 
[Run App](https://diabetespredection.onrender.com/)

### Software and tools requirements 

1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/downloads)
4. [RenderAccount](https://render.com)

Create a new environment to run it on local machine

```
conda create -p diaenv python==3.7 -y
```
Activate the environment
```
conda activate diaenv/
```

### About files 

1. main.py => Application file
2. knn_model.pkl => Pickle file for knn model 
3. lr_model.pkl => Pickle file for logestic regression model
4. diabetes_predection.ipynb => All data preprocessings and model training is done in this notebook. 
5. requirements.txt => All the libraries used in the project

### About sub repositories

1. templates => contains index.html(html template for the project) 
2. static => contains static files(styles.css and images)
3. data_sets => contains csv files used in training