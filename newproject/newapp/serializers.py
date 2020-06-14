from rest_framework import serializers
from newapp.models import boot
class bootSerializer(serializers.Serializer):
    Name = serializers.CharField(max_length=20)
    Email = serializers.EmailField()
    Password = serializers.CharField(max_length=20)
    def create(self, validate_data):
        return boot.objects.create(**validate_data)