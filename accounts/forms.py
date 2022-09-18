from django import forms
from django.contrib.auth.models import User

continents = (
    ('africa', 'Africa'),
    ('asia', 'Asia'),
    ('europe', 'Europe'),
    ('north america', 'North America'),
    ('south america', 'South America'),
    ('antarctica', 'Antarctica'),
)


class RegForm(forms.Form):

    username = forms.CharField(max_length=250)
    first_name = forms.CharField(max_length=250)
    surname = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=60)
    phone_number = forms.IntegerField(min_value=0)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200)
    continent = forms.ChoiceField(choices=continents)

    def clean_username(self):
        username = self.cleaned_data.get("username")
    
        return username

    def clean_firstname(self):
        first_name = self.cleaned_data.get("first_name")
        
        return first_name

    def clean_surname(self):
        surname = self.cleaned_data.get("surname")
        
        return surname

    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        
        return phone_number
    
    def clean_continent(self):
        continent = self.cleaned_data.get("continent")
        
        return continent

    def clean_password(self):
        password = self.cleaned_data.get("password")
        
        return password
    

class LoginForm(forms.Form):

    username = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=200)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        return password

class UpdateForm(forms.Form):
    first_name = forms.CharField(max_length=250)
    surname = forms.CharField(max_length=250)
    email = forms.EmailField(max_length=60)
    phone_number = forms.IntegerField(min_value=0)
    continent = forms.ChoiceField(choices=continents)

    def clean_firstname(self):
        first_name = self.cleaned_data.get("first_name")
        
        return first_name

    def clean_surname(self):
        surname = self.cleaned_data.get("surname")
        
        return surname

    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        
        return phone_number
    
    def clean_continent(self):
        continent = self.cleaned_data.get("continent")
        
        return continent
    
