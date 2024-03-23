from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from cardbackend.admin import admin_site
from cardapp.models import Card
# Register your models here.

class CardResource(resources.ModelResource):
  class Meta:
      model = Card
      fields = ('id', 'name_of_owner', 'email_of_owner', 'number')

class CardAdmin(ImportExportModelAdmin):
  resource_class = CardResource
  list_display = ('id', 'name_of_owner', 'email_of_owner', 'number')

admin_site.register(Card, CardAdmin)   