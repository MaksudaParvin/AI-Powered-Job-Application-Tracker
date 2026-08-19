from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import JobApplicationForm, InterviewForm
from .models import JobApplication, Interview

from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.db.models import Q, Count

from django.utils import timezone


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



@login_required
def dashboard_view(request):

    user = request.user

    # ========================================
    # TOTAL APPLICATIONS
    # ========================================

    total_applications = JobApplication.objects.filter(
        user=user
    ).count()


    # ========================================
    # APPLICATION STATUS COUNTS
    # ========================================

    status_counts = (
        JobApplication.objects
        .filter(user=user)
        .values('status')
        .annotate(count=Count('id'))
    )


    status_data = {
        'wishlist': 0,
        'applied': 0,
        'screening': 0,
        'interview': 0,
        'selected': 0,
        'rejected': 0,
    }


    for item in status_counts:

        status = item['status']

        if status in status_data:

            status_data[status] = item['count']


    # ========================================
    # RECENT APPLICATIONS
    # ========================================

    applications = (
        JobApplication.objects
        .filter(user=user)
        .order_by('-created_at')[:5]
    )


    # ========================================
    # UPCOMING INTERVIEWS
    # ========================================

    today = timezone.localdate()


    upcoming_interviews = (
        Interview.objects
        .filter(
            application__user=user,
            interview_date__gte=today
        )
        .select_related('application')
        .order_by(
            'interview_date',
            'interview_time'
        )[:3]
    )


    # ========================================
    # INTERVIEW COUNT
    # ========================================

    interview_count = (
        Interview.objects
        .filter(
            application__user=user,
            interview_date__gte=today
        )
        .count()
    )


    # ========================================
    # CONTEXT
    # ========================================

    context = {

        'total_applications':
            total_applications,

        'status_data':
            status_data,

        'applications':
            applications,

        'upcoming_interviews':
            upcoming_interviews,

        'interview_count':
            interview_count,
    }


    return render(
        request,
        'dashboard.html',
        context
    )


def interview_list_view(request):

    interviews = Interview.objects.filter(
        application__user=request.user
    ).select_related(
        'application'
    ).order_by(
        'interview_date',
        'interview_time'
    )

    return render(
        request,
        'interviews/interview_list.html',
        {
            'interviews': interviews
        }
    )


@login_required
def create_interview_view(request):

    if request.method == 'POST':

        form = InterviewForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():

            interview = form.save(
                commit=False
            )

            # Extra security check
            if interview.application.user != request.user:

                form.add_error(
                    'application',
                    'Invalid application selected.'
                )

            else:

                interview.save()

                messages.success(
                    request,
                    'Interview scheduled successfully.'
                )

                return redirect(
                    'interview_list'
                )

    else:

        form = InterviewForm(
            user=request.user
        )

    return render(
        request,
        'applications/interview_form.html',
        {
            'form': form,
            'page_title': 'Add Interview',
        }
    )


@login_required
def interview_detail_view(request, pk):

    interview = get_object_or_404(
        Interview,
        pk=pk,
        application__user=request.user
    )

    return render(
        request,
        'applications/interview_detail.html',
        {
            'interview': interview
        }
    )

@login_required
def edit_interview_view(request, pk):

    interview = get_object_or_404(
        Interview,
        pk=pk,
        application__user=request.user
    )

    if request.method == 'POST':

        form = InterviewForm(
            request.POST,
            instance=interview,
            user=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Interview updated successfully.'
            )

            return redirect(
                'interview_list'
            )

    else:

        form = InterviewForm(
            instance=interview,
            user=request.user
        )

    return render(
        request,
        'applications/interview_form.html',
        {
            'form': form,
            'page_title': 'Edit Interview',
            'interview': interview,
        }
    )


@login_required
def delete_interview_view(request, pk):

    interview = get_object_or_404(
        Interview,
        pk=pk,
        application__user=request.user
    )

    if request.method == 'POST':

        interview.delete()

        messages.success(
            request,
            'Interview deleted successfully.'
        )

        return redirect(
            'interview_list'
        )

    return redirect(
        'interview_list'
    )