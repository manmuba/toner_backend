from django.shortcuts import render, get_object_or_404
from rest_framework import generics, pagination, status
from rest_framework.response import Response
from .models import PersonalInformation
from .serializers import PersonalInformationSerializer

# Create your views here.

class PersonalInfo(generics.ListCreateAPIView):
    serializer_class = PersonalInformationSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = PersonalInformation.objects.filter(user=user)
            return queryset
        return Response({"response": "User must logged in"})
    
class PersonalInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonalInformationSerializer
    queryset = PersonalInformation