from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.custom_logout, name='logout'),  # Ahora usa la vista personalizada
    path('editar/', views.editar_view, name='editar'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),  
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
]
