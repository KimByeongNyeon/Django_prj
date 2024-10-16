from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, SignupView, 
    UserUpdateView, UserDeleteView
)

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('delete/', UserDeleteView.as_view(), name='delete'),
]
