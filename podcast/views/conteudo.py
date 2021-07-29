from django.shortcuts import render
from rest_framework import viewsets, mixins

# Create your views here.
from podcast.models import ConteudoModel
from podcast.serializers import ConteudoSerializer


class ConteudoView(viewsets.ModelViewSet, ):
    queryset = ConteudoModel.objects.all()
    serializer_class = ConteudoSerializer

