from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name='api'

urlpatterns = [
    path('', views.IndexView.as_view(), name='root'),
    path('albums/', views.AlbumsView.as_view(), name='albums'),
    path('albums/<int:artistid>/', views.AlbumsView.as_view(), name='albums-by-artist'),
    path('artists/', views.ArtistsView.as_view(), name='artists'),
    path('artists/<str:name>/', views.ArtistsView.as_view(), name='artists-by-name'),
    path('invoices/', views.InvoicesView.as_view(), name='invoices'),
    path('invoices/<int:customerid>/', views.InvoicesView.as_view(), name='invoices-by-customer'),
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('invoiceitems/', views.InvoiceItemsView.as_view(), name='invoiceitems'),
    path('token/', obtain_auth_token, name='token')

]