from rest_framework import serializer
from .models import libros 

class librosSerializer(serializer.ModelSerializer):
    class Meta:
        model = libros      
        fields = '__all__'