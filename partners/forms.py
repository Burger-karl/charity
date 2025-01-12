from django import forms
from .models import Partner, Volunteer

# Forms
class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'email', 'phone_number', 'organization', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization (Optional)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 4}),
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'availability', 'skills', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Availability (e.g., Weekends, Full-time)'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Skills', 'rows': 4}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message (Optional)', 'rows': 4}),
        }
