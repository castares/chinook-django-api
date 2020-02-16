from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'albums', views.AlbumsViewSet)
router.register(r'artists', views.ArtistsViewSet)
router.register(r'invoices', views.InvoicesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls'))

]