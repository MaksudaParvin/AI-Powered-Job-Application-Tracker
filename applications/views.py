from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import JobApplicationForm
from .models import JobApplication

from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.db.models import Q


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

    # Search
    search = request.GET.get(
        'search',
        ''
    ).strip()

    if search:

        applications = applications.filter(
            Q(job_title__icontains=search) |
            Q(company_name__icontains=search)
        )


    # Status
    status = request.GET.get(
        'status',
        ''
    )

    if status:

        applications = applications.filter(
            status=status
        )


    # Category
    category = request.GET.get(
        'category',
        ''
    )

    if category:

        applications = applications.filter(
            category=category
        )


    # Location
    location = request.GET.get(
        'location',
        ''
    ).strip()

    if location:

        applications = applications.filter(
            location__icontains=location
        )


    # Sorting
    sort = request.GET.get(
        'sort',
        'newest'
    )

    if sort == 'oldest':

        applications = applications.order_by(
            'application_date'
        )

    elif sort == 'company':

        applications = applications.order_by(
            'company_name'
        )

    elif sort == 'title':

        applications = applications.order_by(
            'job_title'
        )

    else:

        applications = applications.order_by(
            '-application_date',
            '-created_at'
        )


    return render(
        request,
        'applications/list.html',
        {
            'applications': applications,

            'search': search,

            'selected_status': status,

            'selected_category': category,

            'selected_location': location,

            'selected_sort': sort,
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