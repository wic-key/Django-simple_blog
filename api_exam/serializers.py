from rest_framework import serializers
from api_exam.models import Language

class LanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Language
        fields = ['id','name','paradiagm']
