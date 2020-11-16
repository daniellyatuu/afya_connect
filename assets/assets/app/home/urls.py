from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about-us/', views.AboutUs.as_view(), name='about_us'),
    path('team/', views.Team.as_view(), name='team'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('contact-us/', views.ContactUs.as_view(), name='contact_us'),
    path('artical/<int:pk>/', views.Artical.as_view(), name='artical'),
]
