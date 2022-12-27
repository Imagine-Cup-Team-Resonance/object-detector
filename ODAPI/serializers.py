from rest_framework import serializers
from .models import image

class imageSerializers(serializers.ModelSerializer):
    class Meta:
        model = image
        fields='__all__'
        