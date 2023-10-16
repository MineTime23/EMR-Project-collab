from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient  # 사용할 모델
        fields = ['last_name', 'first_name', 'birth_date', 'address', 'gender', 'phone_num', 'email', 'image']
