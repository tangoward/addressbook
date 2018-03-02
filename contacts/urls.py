from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='contacts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('create/', views.CreateContact.as_view(), name='create_contact'),
    path('update/<int:pk>', views.UpdateContact.as_view(), name='update_contact'),
    path('delete/<int:pk>', views.DeleteContact.as_view(), name='delete_contact'),
    path('csv/', views.CsvView.as_view(), name='csv_import'),
]
