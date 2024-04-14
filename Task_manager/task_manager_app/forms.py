from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


from .models import User, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            try:
                validate_email(email)
            except ValidationError:
                raise forms.ValidationError("Invalid email format")
            return email

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'task_detail', 'task_type']




    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Invalid email format")
        return email