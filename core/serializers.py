from rest_framework import serializers
from .models import job,application,user

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=job
        fields='__all__'