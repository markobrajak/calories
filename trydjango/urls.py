"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from pages.views import home_view, profile_view, calories_view, add_food_view, registration_successful_view, logout_successful_view, create_new_food_view, add_exercise_view, create_new_exercise_view
from userregister import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('my-profile', profile_view, name='profile'),
    path('calories', calories_view, name='calories'),
    path('add-food', add_food_view, name='add-food'),
    path('add-exercise', add_exercise_view, name='add-exercise'),
    path('register', v.register, name="register"),
    path('registration-successful', registration_successful_view, name="registration-successful"),
    path('create-food', create_new_food_view, name="create_new_food_view"),
    path('create-exercise', create_new_exercise_view, name="create_new_exercise_view"),
    path('', include('django.contrib.auth.urls')),
    path('logout-successful', logout_successful_view, name='logout'),
]
