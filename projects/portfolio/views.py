
from .models import *
from .serializers import *
from rest_framework import generics



class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ProjectsAPIView(generics.ListAPIView):
    queryset = Projects.objects.all() #.order_by('updatedAt'-1)
    serializer_class = ProjectsSerializer

class AchievementsAPIView(generics.ListAPIView):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

class AcademicAPIView(generics.ListAPIView):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer

class JobsAPIView(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
