# rest_framework imports
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.reverse import reverse

# Local imports
from .serializers import AlbumsSerializer, ArtistsSerializer, InvoicesSerializer
from .models import Albums, Artists, Invoices


# Viewsets
class AlbumsViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumsSerializer
    queryset = Albums.objects.all().order_by('albumid')


class ArtistsViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistsSerializer
    queryset = Artists.objects.all().order_by('artistid')


# Class-based views
class InvoicesView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = InvoicesSerializer
    queryset = Invoices.objects.all().order_by('invoiceid')


# Function-based views
@api_view(['GET', ])
@permission_classes([IsAuthenticated])
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


