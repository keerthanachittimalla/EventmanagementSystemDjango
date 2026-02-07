from django.urls import path
from . import views
urlpatterns = [

    path('signuppage/',views.signup,name="signuppage"),
    path('signuppage/accounts/signup',views.signupinfo,name="signup"),
    path('login',views.login,name="login"),
    path('accounts/userhome',views.login,name="userhome"),
    path('logout',views.logout,name="logout"),
]