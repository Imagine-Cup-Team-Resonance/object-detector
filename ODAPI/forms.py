from django import forms

class ImageForm(forms.Form):
    object_image = forms.ImageField()
    background_image = forms.ImageField()
    description=forms.CharField(max_length=30)