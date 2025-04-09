from django import  forms
from .models import Question, Comments
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label="Password")

    class Meta:
        model = User
        fields = ['username','password']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password =  forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']

    def validate_password(self):
         password = self.cleaned_data['password']
         confirm_password = self.confirm_password['confirm_password']

         if  password != confirm_password:
             raise forms.ValidationError("Password & Confirm Password is not Matched")
         else:
            return confirm_password

class QuestionForm(forms.ModelForm):
    class Meta:
        model  = Question
        fields = ['title','description']

class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model  = Question
        fields = ['title','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comments
        fields = ['description']

