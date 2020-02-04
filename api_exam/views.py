from django.shortcuts import render
from api_exam.serializers import LanguageSerializer
from api_exam.models import Language
from rest_framework import viewsets

class LaguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

