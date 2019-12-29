from django.urls import path
from . import views

urlpatterns = [
    path('api/login', views.user_login),
    path('api/get-all-user', views.get_all_user),
    path('api/dashboard', views.dashboard),
    path('api/single-inspection', views.find_single_inspection),
    path('api/set-fine-amount', views.set_fine_amount),
    path('api/create-inspection', views.create_inspection),
]
