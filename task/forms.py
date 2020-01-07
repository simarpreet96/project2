from django import forms
from .models import Details, Country, City 
from .validators import validate_file_extension2


class DetailsForm(forms.ModelForm):
    image = forms.FileField(validators=[validate_file_extension2])
    class Meta:
        model = Details
        fields = ('name', 'email','address','country','city','zipcode','phone_number','image')
    
