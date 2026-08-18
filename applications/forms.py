from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'job_title',
            'company_name',
            'job_description',
            'location',
            'salary',
            'job_url',
            'application_date',
            'status',
            'category',
            'notes',
        ]

        widgets = {

            'job_title': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Python Developer'
                }
            ),

            'company_name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Google'
                }
            ),

            'job_description': forms.Textarea(
                attrs={
                    'placeholder': 'Paste the job description here...',
                    'rows': 6
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Dhaka / Remote'
                }
            ),

            'salary': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. 50,000 - 70,000 BDT'
                }
            ),

            'job_url': forms.URLInput(
                attrs={
                    'placeholder': 'https://...'
                }
            ),

            'application_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'placeholder': 'Add any notes...',
                    'rows': 4
                }
            ),
        }