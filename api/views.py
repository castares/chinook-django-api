# rest_framework imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404

# Local imports
from .serializers import AlbumsSerializer, ArtistsSerializer, InvoicesSerializer
from .models import Albums, Artists, Invoices

class IndexView(APIView):

    def get(self, request):
        endpoints = {

            'albums' : reverse('api:albums', request=request),
            'albums by artist' : reverse('api:albums-by-artist', args=[1], request=request),
            'artists' : reverse('api:artists', request=request),
            'artists by name' : reverse('api:artists-by-name', args=['Accept'], request=request),
            'invoices' : reverse('api:invoices', request=request)
       
         }
        return Response(endpoints)

class ArtistsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArtistsSerializer
    queryset = Artists.objects.all().order_by('artistid')
    lookup_field='name'

    def get(self, request, name=None):
        if name:
            return self.retrieve(request, name)
        return self.list(request)

class AlbumsView(generics.ListAPIView):
    serializer_class = AlbumsSerializer
    lookup_field='artistid'

    def get_queryset(self):
        artistid = self.kwargs.get(self.lookup_field)
        if artistid:
            queryset = Albums.objects.filter(artistid=artistid).order_by('albumid')
        else:
            queryset = Albums.objects.all().order_by('albumid')
        return queryset

class InvoicesView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    serializer_class = InvoicesSerializer
    queryset = Invoices.objects.all().order_by('invoiceid')
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('billingcity','billingstate', 'customerid_id__firstname', 'customerid_id__lastname')
    ordering_fields = ('invoiceid')

class CustomersView(generics.ListCreateAPIView, mixins.UpdateModelMixin):
    pass

