from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers
from .models import food 

class foodserializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'

class foodview(ListCreateAPIView):
    queryset = food.objects.all()
    serializer_class = foodserializer

class foodByID(RetrieveUpdateDestroyAPIView):
    queryset = food.objects.all()
    serializer_class = foodserializer