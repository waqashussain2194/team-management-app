from django import forms
from django.core.exceptions import ValidationError
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email