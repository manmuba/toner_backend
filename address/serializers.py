from rest_framework import serializers
from .models import PersonalInformation

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = '__all__'