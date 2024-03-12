from django.shortcuts import render
import numpy as np
from predictor.forms import HeartDiseaseForm
from joblib import load


def heart(request):
    model =load('./savedModels/model.joblib')
    value = ''
    if request.method == 'POST':
        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

  
        user_data = np.array(
            (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        ).reshape(1, -1)
        prediction = model.predict(user_data)

         # Determine the result based on the prediction
        if prediction[0] == 1:
            value = 'have'
        elif prediction[0] == 0:
            value = "don\'t have"

    return render(request,
                  'heart.html',
                  {
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': HeartDiseaseForm(),
                  })

def home(request):

    return render(request,
                  'home.html')





