from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('verify_user_authentication', views.verify_user_authentication, name='verify_user_authentication'),
]