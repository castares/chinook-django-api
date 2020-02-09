from rest_framework import serializers
from api import models



class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Albums
        fields = ('albumid', 'title', 'artistid')