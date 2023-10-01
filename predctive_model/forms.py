from django import forms

class PredictionForm(forms.Form):
    input_data = forms.CharField(max_length=100)
    image_upload = forms.FileField()
