from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('',views.index, name='home'),
    path('about/',views.about, name='about'),
    path('prediction/',views.prediction, name='prediction'),
    path('contact/',views.contact, name='contact'),
    path('logout/', views.logout_view, name='logout'),
]
