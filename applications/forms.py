from django import forms
from .models import JobApplication, Interview


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


class InterviewForm(forms.ModelForm):

    class Meta:

        model = Interview

        fields = [
            'application',
            'interview_date',
            'interview_time',
            'interview_type',
            'meeting_link',
            'notes',
        ]

        widgets = {

            'application': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'interview_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'interview_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),

            'interview_type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'meeting_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://meet.google.com/...'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Add interview notes...'
                }
            ),
        }

    def __init__(self, *args, user=None, **kwargs):

        super().__init__(*args, **kwargs)

        if user:

            self.fields[
                'application'
            ].queryset = JobApplication.objects.filter(
                user=user
            ).order_by(
                'company_name',
                'job_title'
            )