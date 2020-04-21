from django.db import models


class Albums(models.Model):
    albumid = models.AutoField(db_column='AlbumId', primary_key=True)
    title = models.CharField(db_column='Title', max_length=160)
    artistid = models.ForeignKey('Artists', db_column='ArtistId', on_delete=models.CASCADE )

    class Meta:
        managed = True
        db_table = 'albums'


class Artists(models.Model):
    artistid = models.AutoField(db_column='ArtistId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=160, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'artists'

class Customers(models.Model):
    customerid = models.AutoField(db_column='CustomerId', primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=160)
    lastname = models.CharField(db_column='LastName', max_length=160)
    company = models.CharField(db_column='Company', max_length=160, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=160, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=160, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=160, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=160, blank=True, null=True)
    postalcode = models.CharField(db_column='PostalCode', max_length=160, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=160, blank=True, null=True)
    fax = models.CharField(db_column='Fax', max_length=160, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=160)
    supportrepid = models.ForeignKey('Employees', db_column='SupportRepId', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeId', primary_key=True)
    lastname = models.CharField(db_column='LastName', max_length=160)
    firstname = models.CharField(db_column='FirstName', max_length=160)
    title = models.CharField(db_column='Title', max_length=160, blank=True, null=True)
    reportsto = models.IntegerField(db_column='ReportsTo', blank=True, null=True)
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=160, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=160, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=160, blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=160, blank=True, null=True)
    postalcode = models.CharField(db_column='PostalCode', max_length=160, blank=True, null=True)
    phone = models.CharField(db_column='Phone', max_length=160, blank=True, null=True)
    fax = models.CharField(db_column='Fax',  max_length=160, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=160, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'employees'


class InvoiceItems(models.Model):
    invoicelineid = models.AutoField(db_column='InvoiceLineId', primary_key=True)
    invoiceid = models.ForeignKey('Invoices', db_column='InvoiceId', on_delete=models.CASCADE)
    trackid = models.IntegerField(db_column='TrackId')
    unitprice = models.CharField(db_column='UnitPrice', max_length=160)
    quantity = models.IntegerField(db_column='Quantity')

    class Meta:
        managed = True
        db_table = 'invoice_items'


class Invoices(models.Model):
    invoiceid = models.AutoField(db_column='InvoiceId', primary_key=True)
    customerid = models.ForeignKey('Customers', db_column='CustomerId', on_delete=models.PROTECT)
    invoicedate = models.DateTimeField(db_column='InvoiceDate')
    billingaddress = models.CharField(db_column='BillingAddress', max_length=160, blank=True, null=True)
    billingcity = models.CharField(db_column='BillingCity', max_length=160, blank=True, null=True)
    billingstate = models.CharField(db_column='BillingState', max_length=160, blank=True, null=True)
    billingcountry = models.CharField(db_column='BillingCountry', max_length=160, blank=True, null=True)
    billingpostalcode = models.CharField(db_column='BillingPostalCode', max_length=160, blank=True, null=True)
    total = models.CharField(db_column='Total', max_length=160)

    class Meta:
        managed = True
        db_table = 'invoices'
        
class Genres(models.Model):
    genreid = models.AutoField(db_column='GenreId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=160)

    class Meta:
        managed = True
        db_table = 'genres'

class MediaTypes(models.Model):
    mediatypeid = models.AutoField(db_column='MediaTypeId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=160)

    class Meta:
        managed = True
        db_table = 'media_types'


class Playlists(models.Model):
    playlistid = models.AutoField(db_column='PlaylistId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=160)

    class Meta:
        managed = True
        db_table = 'playlists'


class PlaylistTrack(models.Model):
    id = models.AutoField(primary_key=True)
    playlistid = models.ForeignKey("Playlists", db_column='PlaylistId', on_delete=models.CASCADE)
    trackid = models.ForeignKey("Tracks", db_column='TrackId', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'playlist_track'


class Tracks(models.Model):
    trackid = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.CharField(db_column='Name', max_length=160) 
    albumid = models.ForeignKey('Albums', db_column='AlbumId', on_delete=models.CASCADE)
    mediatypeid = models.ForeignKey('MediaTypes', db_column='MediaTypeId', on_delete=models.CASCADE)
    genreid = models.ForeignKey('Genres', db_column='GenreId', on_delete=models.CASCADE)
    composer = models.CharField(db_column='Composer', max_length=160, blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unitprice = models.CharField(db_column='UnitPrice', max_length=160)

    class Meta:
        managed = True
        db_table = 'tracks'



