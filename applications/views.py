from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def create_application_view(request):

    if request.method == 'POST':

        form = JobApplicationForm(request.POST)

        if form.is_valid():

            application = form.save(
                commit=False
            )

            application.user = request.user

            application.save()

            return redirect('dashboard')

    else:

        form = JobApplicationForm()

    return render(
        request,
        'applications/create.html',
        {
            'form': form
        }
    )


@login_required
def application_list_view(request):

    applications = JobApplication.objects.filter(
        user=request.user
    )

    return render(
        request,
        'applications/list.html',
        {
            'applications': applications
        }
    )