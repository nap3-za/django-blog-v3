from django.urls import path 
from .views import RegView, LoginView, LogoutView, MyAccView, UpdateAccView, DeleteAccountView


urlpatterns = [
    path('accounts/register/', RegView, name="regview"),
    path('accounts/login/', LoginView, name="loginview"),
    path('accounts/logout/', LogoutView, name="logoutview"),
    path('accounts/my-account/', MyAccView, name="myaccview"),
    path('accounts/update/', UpdateAccView, name="updateview"),
    path('account/delete/', DeleteAccountView, name="deleteaccview")

]
