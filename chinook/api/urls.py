from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name='api'

# router = routers.DefaultRouter()
# router.register(r'albums', views.AlbumsViewSet)
# router.register(r'artists', views.ArtistsViewSet)
# router.register(r'invoices', views.InvoicesView)

urlpatterns = [
    path('albums/', views.AlbumsView.as_view(), name='albums'),
    path('albums/<int:artistid>/', views.AlbumsView.as_view(), name='albums-by-artist'),
    path('artists/', views.ArtistsView.as_view(), name='artists'),
    path('artists/<str:name>/', views.ArtistsView.as_view(), name='artists-by-name'),
    path('invoices/', views.InvoicesView.as_view(), name='invoices'),
    path('token/', obtain_auth_token, name='login')

]