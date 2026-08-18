from django.conf import settings
from django.db import models


class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('wishlist', 'Wishlist'),
        ('applied', 'Applied'),
        ('screening', 'Screening'),
        ('interview', 'Interview'),
        ('selected', 'Selected'),
        ('rejected', 'Rejected'),
    ]

    CATEGORY_CHOICES = [
        ('software', 'Software Engineering'),
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('fullstack', 'Full Stack Development'),
        ('design', 'UI / UX Design'),
        ('data', 'Data / AI'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )

    job_title = models.CharField(
        max_length=200
    )

    company_name = models.CharField(
        max_length=200
    )

    job_description = models.TextField()

    location = models.CharField(
        max_length=200
    )

    salary = models.CharField(
        max_length=100,
        blank=True
    )

    job_url = models.URLField(
        blank=True
    )

    application_date = models.DateField(
        null=True,
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='other'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='wishlist'
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.job_title} - {self.company_name}'


class Interview(models.Model):

    INTERVIEW_TYPE_CHOICES = [
        ('video', 'Video Call'),
        ('phone', 'Phone Call'),
        ('onsite', 'On-site'),
        ('technical', 'Technical Interview'),
        ('hr', 'HR Interview'),
        ('other', 'Other'),
    ]

    application = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        related_name='interviews'
    )

    interview_date = models.DateField()

    interview_time = models.TimeField()

    interview_type = models.CharField(
        max_length=30,
        choices=INTERVIEW_TYPE_CHOICES,
        default='video'
    )

    meeting_link = models.URLField(
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            'interview_date',
            'interview_time'
        ]

    def __str__(self):
        return (
            f'{self.application.company_name} - '
            f'{self.application.job_title}'
        )