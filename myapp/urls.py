from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]