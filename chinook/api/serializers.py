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

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customers
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = '__all__'

class InvoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceItems
        fields = '__all__'

class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoices
        fields = '__all__'
        depth = 1

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genres
        fields = '__all__'

class MediaTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaTypes
        fields = '__all__'

class PlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Playlists
        fields = '__all__'

class PlaylistTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlaylistTrack
        fields = '__all__'

class Tracks(serializers.ModelSerializer):
    class Meta:
        model = models.PlaylistTrack
        fields = '__all__'   