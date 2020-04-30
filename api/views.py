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
from .serializers import (
    AlbumsSerializer, 
    ArtistsSerializer, 
    InvoicesSerializer,
    CustomersSerializer,
    InvoiceItemsSerializer

    
)
from .models import (
    Albums, Artists, Invoices, Customers, InvoiceItems,
)
class IndexView(APIView):

    def get(self, request):
        endpoints = {

            'albums' : reverse('api:albums', request=request),
            'albums by artist' : reverse('api:albums-by-artist', args=[1], request=request),
            'artists' : reverse('api:artists', request=request),
            'artists by name' : reverse('api:artists-by-name', args=['Accept'], request=request),
            'invoices' : reverse('api:invoices', request=request),
            'invoices-by-customer' : reverse('api:invoices-by-customer', args=[1], request=request),
            'customers' : reverse('api:customers', request=request),
            'customer-by-id' : reverse('api:customer-by-id', args=[1], request=request),
            'invoiceitems' : reverse('api:invoiceitems', request=request)
       
         }
        return Response(endpoints)

class ArtistsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArtistsSerializer
    pagination_class = PageNumberPagination
    queryset = Artists.objects.all().order_by('artistid')
    lookup_field='name'

    def get(self, request, name=None):
        if name:
            return self.retrieve(request, name)
        return self.list(request)

class AlbumsView(generics.ListAPIView):
    serializer_class = AlbumsSerializer
    pagination_class = PageNumberPagination
    lookup_field='artistid'

    def get_queryset(self):
        artistid = self.kwargs.get(self.lookup_field)
        if artistid:
            queryset = Albums.objects.filter(artistid=artistid).order_by('albumid')
        else:
            queryset = Albums.objects.all().order_by('albumid')
        return queryset

class InvoicesView(generics.ListAPIView, mixins.RetrieveModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    serializer_class = InvoicesSerializer
    queryset = Invoices.objects.all().order_by('invoiceid')
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('billingcity','billingstate', 'customerid_id__firstname', 'customerid_id__lastname')
    ordering_fields = ('invoiceid')
    lookup_field = 'customerid'

    def get(self, request, customerid=None):
        if customerid:
            return self.retrieve(request, customerid)
        return self.list(request)        

class CustomersView(generics.ListAPIView, mixins.RetrieveModelMixin):
    pagination_class = PageNumberPagination
    serializer_class = CustomersSerializer     
    queryset = Customers.objects.all().order_by('customerid')

    def get(self, request, pk=None):
        """
        pk maps to customerid
        """
        if pk:
            return self.retrieve(request, pk)
        return self.list(request)

class InvoiceItemsView(generics.ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = InvoiceItemsSerializer
    queryset = InvoiceItems.objects.all().order_by('invoiceid')

    def get(self, request, **kwargs):
        invoiceid = self.request.query_params.get("invoiceid", None)
        if invoiceid:
            self.queryset = InvoiceItems.objects.filter(invoiceid=invoiceid).order_by('invoiceid','invoicelineid')
        return self.list(request)






