from rest_framework import serializers
from Monitor.models import Plant, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','plant','userId', '')


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('serial', 'name')