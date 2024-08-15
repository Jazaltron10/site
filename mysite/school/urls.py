from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('king/<str:name>/', views.king_view, name='king'),
    path('welcome-class/', views.WelcomeView.as_view(), name='welcome_class'),
    path('list-class/', views.ListView.as_view(), name='list_class'),
    path('students/', views.ListStudentsView.as_view(), name='list-students'),
    path('courses/', views.ListCoursesView.as_view(), name='list-courses'),
    path('allcourses/', views.ListAllView.as_view(), name='list-all-courses'),
]


