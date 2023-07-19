from . models import Task
from django import forms
class TODOForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']