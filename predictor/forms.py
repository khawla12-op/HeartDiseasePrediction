from django import forms
 
class HeartDiseaseForm(forms.Form):
    # Define form fields for heart disease prediction
 
    age = forms.FloatField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for age, represented as a float input widget
 
    sex = forms.FloatField(label='Sex', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for sex, represented as a float input widget
 
    cp = forms.FloatField(label='CP', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for chest pain type (CP), represented as a float input widget
 
    trestbps = forms.FloatField(label='TRESTBPS', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for resting blood pressure (TRESTBPS), represented as a float input widget
 
    chol = forms.FloatField(label='CHOL', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for serum cholesterol level (CHOL), represented as a float input widget
 
    fbs = forms.FloatField(label='FBS', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for fasting blood sugar (FBS), represented as a float input widget
 
    restecg = forms.FloatField(label='RESTECG', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for resting electrocardiographic results (RESTECG), represented as a float input widget
 
    thalach = forms.FloatField(label='THALACH', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for maximum heart rate achieved (THALACH), represented as a float input widget
 
    exang = forms.FloatField(label='EXANG', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for exercise-induced angina (EXANG), represented as a float input widget
 
    oldpeak = forms.FloatField(label='OLDPEAK', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for ST depression induced by exercise relative to rest (OLDPEAK), represented as a float input widget
 
    slope = forms.FloatField(label='SLOPE', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for the slope of the peak exercise ST segment (SLOPE), represented as a float input widget
 
    ca = forms.FloatField(label='CA', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for the number of major vessels colored by fluoroscopy (CA), represented as a float input widget
 
    thal = forms.FloatField(label='THAL', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # Field for thalassemia (THAL), represented as a float input widget