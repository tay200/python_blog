from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #http://localhost:8000/pybo/common/signup/ 페이지가 요청되면 views.signup 함수가 실행
    path('signup/', views.signup, name='signup'),
]