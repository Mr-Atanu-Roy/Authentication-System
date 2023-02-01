from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout, name="logout"),
    path('email-verify/<token>', email_verify, name="email_verify"),
    path('reset-password/', resetPassword, name="reset_password"),
    path('reset-password/<token>', resetPasswordLink, name="reset_password_link"),
]