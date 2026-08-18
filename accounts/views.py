from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def register_view(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('login')

    else:

        form = RegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid email or password.'
            }
        )

    return render(
        request,
        'accounts/login.html'
    )

def logout_view(request):

    logout(request)

    return redirect('login')


@login_required
def dashboard_view(request):

    return render(
        request,
        'dashboard.html'
    )