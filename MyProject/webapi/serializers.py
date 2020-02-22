from rest_framework import serializers
from .models import Alert
from django.contrib.auth.models import User


class AlertSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Alert
        fields = ['id','title', 'owner']

class UserSerializer(serializers.ModelSerializer):
    alert = serializers.PrimaryKeyRelatedField(many=True, queryset=Alert.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'alert']