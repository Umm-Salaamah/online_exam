from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('exam_list', views.exam_list, name='exam_list'),
    path('create_exam/', views.create_exam, name='create_exam'),
    path('create_question/', views.create_question, name='create_question'),
    path('take_exam/<int:exam_id>/', views.take_exam, name='take_exam'),
]