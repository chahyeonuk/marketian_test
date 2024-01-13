from .models import Board
from django import forms

class BoardForm(forms.ModelForm):
    file = forms.FileField(required=False)
    
    class Meta:
        model = Board
        fields = ('title', 'text', 'file')

