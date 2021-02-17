from django.urls import path
from django.contrib.auth import views
from .views import MyAccountView, ShowView, EditView
app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='account/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='account/logout.html', next_page='account:login'), name='logout'),
    path('myaccount/', view=MyAccountView.as_view(), name="myaccount"),
    path('myacount/show/', view=ShowView.as_view(), name="show"),
    path('myaccount/edit/', view=EditView.as_view(), name="edit"),
]