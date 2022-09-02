from django.urls import path

from searchapp import views #as sv

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('counter/', views.counter, name="counter")
    ]