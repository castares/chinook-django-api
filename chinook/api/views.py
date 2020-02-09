from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AlbumsSerializer
from .models import Albums


class AlbumsViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumsSerializer
    queryset = Albums.objects.all().order_by('Albumid')
