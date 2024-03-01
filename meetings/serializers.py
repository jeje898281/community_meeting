from rest_framework import serializers
from .models import Household, Attend

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = '__all__'

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attend
        fields = '__all__'
