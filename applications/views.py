from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import JobApplicationForm
from .models import JobApplication

from django.shortcuts import get_object_or_404
from django.contrib import messages


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



@login_required
def application_detail_view(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        'applications/detail.html',
        {
            'application': application
        }
    )


@login_required
def edit_application_view(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = JobApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            form.save()

            return redirect(
                'application_list',
            )

    else:

        form = JobApplicationForm(
            instance=application
        )

    return render(
        request,
        'applications/edit.html',
        {
            'form': form,
            'application': application
        }
    )



@login_required
def delete_application_view(request, pk):

    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        application.delete()

        messages.success(
            request,
            'Application deleted successfully.'
        )

        return redirect('application_list')

    return redirect(
        'application_detail',
        pk=application.pk
    )