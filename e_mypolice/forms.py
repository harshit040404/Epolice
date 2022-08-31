from django import forms
from .models import login_data,contactus,fir,missingperson,stolenproperty

class loginform(forms.ModelForm):
    class Meta:
        model=login_data
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model= contactus
        fields='__all__'

class firForm(forms.ModelForm):
    class Meta:
        model= fir
        fields='__all__'

class missingpForm(forms.ModelForm):
    class Meta:
        model= missingperson
        fields='__all__'

class stolenForm(forms.ModelForm):
    class Meta:
        model= stolenproperty
        fields='__all__'