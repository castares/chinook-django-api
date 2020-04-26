# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Albums(models.Model):
    albumid = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    artistid = models.ForeignKey('Artists', models.DO_NOTHING, db_column='artistid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'albums'


class Artists(models.Model):
    artistid = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'


class Customers(models.Model):
    customerid = models.BigAutoField(primary_key=True)
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    postalcode = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    supportrepid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='supportrepid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    employeeid = models.BigAutoField(primary_key=True)
    lastname = models.TextField(blank=True, null=True)
    firstname = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='reportsto', blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)
    hiredate = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    postalcode = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Genres(models.Model):
    genreid = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class InvoiceItems(models.Model):
    invoicelineid = models.BigAutoField(primary_key=True)
    invoiceid = models.ForeignKey('Invoices', models.DO_NOTHING, db_column='invoiceid', blank=True, null=True)
    trackid = models.ForeignKey('Tracks', models.DO_NOTHING, db_column='trackid', blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_items'


class Invoices(models.Model):
    invoiceid = models.BigAutoField(primary_key=True)
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    invoicedate = models.DateTimeField(blank=True, null=True)
    billingaddress = models.TextField(blank=True, null=True)
    billingcity = models.TextField(blank=True, null=True)
    billingstate = models.TextField(blank=True, null=True)
    billingcountry = models.TextField(blank=True, null=True)
    billingpostalcode = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    mediatypeid = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_types'


class PlaylistTrack(models.Model):
    playlistid = models.OneToOneField('Playlists', models.DO_NOTHING, db_column='playlistid', primary_key=True)
    trackid = models.ForeignKey('Tracks', models.DO_NOTHING, db_column='trackid')

    class Meta:
        managed = False
        db_table = 'playlist_track'
        unique_together = (('playlistid', 'trackid'), ('playlistid', 'trackid'),)


class Playlists(models.Model):
    playlistid = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)
    idx = models.TextField(blank=True, null=True)
    stat = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Tracks(models.Model):
    trackid = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    albumid = models.ForeignKey(Albums, models.DO_NOTHING, db_column='albumid', blank=True, null=True)
    mediatypeid = models.ForeignKey(MediaTypes, models.DO_NOTHING, db_column='mediatypeid', blank=True, null=True)
    genreid = models.ForeignKey(Genres, models.DO_NOTHING, db_column='genreid', blank=True, null=True)
    composer = models.TextField(blank=True, null=True)
    milliseconds = models.BigIntegerField(blank=True, null=True)
    bytes = models.BigIntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracks'
