from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutAPIView.as_view(), name='about'),
    path('projects/', ProjectsAPIView.as_view(), name='projects'),
    path('achievements/', AchievementsAPIView.as_view(), name='achievements'),
    path('academic/', AcademicAPIView.as_view(), name='academic'),
    path('jobs/', JobsAPIView.as_view(), name='jobs'),
]