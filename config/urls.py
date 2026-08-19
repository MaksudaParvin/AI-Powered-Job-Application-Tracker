"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from accounts.views import (register_view, login_view, logout_view)
from applications.views import (create_application_view, application_list_view,
                                 application_detail_view, edit_application_view,
                                 delete_application_view, dashboard_view, 
                                 interview_list_view, create_interview_view)

urlpatterns = [

    path('register/',register_view, name='register'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view,  name='logout'),

    path('', dashboard_view,  name='dashboard'),   

    path('dashboard/', dashboard_view,  name='dashboard'),

    path('create/', create_application_view,  name='create_application'), 

    path('list/', application_list_view,  name='application_list'),  

    path('applications/<int:pk>/', application_detail_view, name='application_detail'),

    path('applications/<int:pk>/edit/',edit_application_view, name='edit_application'),

    path('applications/<int:pk>/delete/', delete_application_view,name='delete_application'),

    path('interview_list/', interview_list_view,  name='interview_list'),   

    path('interviews/create/', create_interview_view, name='interview_create'),

]
