# rest_framework imports
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Local imports
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


#Function-based views
@api_view(['GET',])
def albumsByArtist(request, artist_name):
    """
    Returns all the albums available by the given artist name
    """
    try:
        artist_id = Artists.objects.get(name=str(artist_name)).artistid
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        albums = Albums.objects.filter(artistid=artist_id)
        serializer = AlbumsSerializer(albums, many=True)
        return Response(serializer.data)
