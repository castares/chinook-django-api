from api import models as api_models
from django.contrib import admin
from django.db.models.base import ModelBase

class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'chinook'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'chinook' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'chinook' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'chinook' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'chinook' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'chinook' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


# Register your models here.

for name, var in api_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)