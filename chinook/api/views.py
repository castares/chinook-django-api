#API Views Imports
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AlbumsSerializer, ArtistsSerializer, InvoicesSerializer
from .models import Albums, Artists, Invoices


class AlbumsViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumsSerializer
    queryset = Albums.objects.all().order_by('albumid')

class ArtistsViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistsSerializer
    queryset = Artists.objects.all().order_by('artistid')

class InvoicesViewSet(viewsets.ModelViewSet):
    serializer_class = InvoicesSerializer
    queryset = Invoices.objects.all().order_by('invoiceid')