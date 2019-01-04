from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    cep = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    neighborhood = serializers.CharField(max_length=200)
    city = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=200)
