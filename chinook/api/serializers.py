from rest_framework import serializers
from api import models



class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Albums
        fields = ('albumid', 'title', 'artistid')

class ArtistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Artists
        fields = ('artistid', 'name')

class InvoicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Invoices
        fields = ('invoiceid', 'customerid','invoicedate','total')