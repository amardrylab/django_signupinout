"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from myapp.views import StudentView
from myapp.views import StudentCreate
from django.views.generic import TemplateView
from home.views import HomeView
from signup.views import SignupView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('list/', StudentView.as_view(), name='list'),
    path('create/', StudentCreate.as_view(), name='create'),
    path('student/<int:pk>', TemplateView.as_view(template_name='myapp/success.html'), name='success'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('success/', TemplateView.as_view(template_name='registration/success.html'), name='success1'),
]
