from django import forms

from .models import Customer, Newspaper, Pomplet, Admin, Horror, Action, Devotional, Insta


class DateInput(forms.DateInput):
    input_type = "date"

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = "__all__"

class PompletForm(forms.ModelForm):
    class Meta:
        model = Pomplet
        fields = "__all__"

class HorrorForm(forms.ModelForm):
    class Meta:
        model = Horror
        fields = "__all__"

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = "__all__"


class DevotionalForm(forms.ModelForm):
    class Meta:
        model = Devotional
        fields = "__all__"

class InstaForm(forms.ModelForm):
    class Meta:
        model = Insta
        fields = "__all__"

class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}
