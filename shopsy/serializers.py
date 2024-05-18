from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'
