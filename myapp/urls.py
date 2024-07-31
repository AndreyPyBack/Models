# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_book/', views.create_book, name='create_book'),
    path('books/', views.book_list, name='book_list'),
    path('create_course/', views.create_course, name='create_course'),
    path('courses/', views.course_list, name='course_list'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profiles/', views.profile_list, name='profile_list'),
]
