from django.urls import path
from app.views import login,registration,homepage
app_name="app"
urlpatterns = [
    path('',login,name='login'),
    path('reg/',registration,name='registration'),
    path('home/',homepage,name='homepage')
]