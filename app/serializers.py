from rest_framework import serializers
from app.models import *

class BikeMS(serializers.ModelSerializer):
    class Meta:
        model=Bike
        fields='__all__'