from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class FormSerializer(serializers.Serializer):
        dining = serializers.IntegerField()
        clothing = serializers.IntegerField()
        gas = serializers.IntegerField()
        others = serializers.IntegerField()
        total = serializers.IntegerField()
