from rest_framework import serializers
from api import models



class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Albums
        fields = ('albumid', 'title', 'artistid')

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artists
        fields = ('artistid', 'name')

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoices
        fields = '__all__'