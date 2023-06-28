from django import forms
from .models import Firm

class FirmForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = ['title', 'main_inf', 'photo', 'location', 'place', 'productions']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'main_inf': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'productions': forms.Select(attrs={'class': 'form-control'}),
        }
