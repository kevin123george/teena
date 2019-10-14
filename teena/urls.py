
from django.contrib import admin
from django.urls import path,include
from brain import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teena/',views.teena),
    path('',views.home),
    path('accounts/', include('django.contrib.auth.urls')),
]