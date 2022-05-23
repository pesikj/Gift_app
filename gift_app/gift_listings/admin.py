# Register your models here.
import gift_listings.models
from django.contrib import admin

admin.site.register(gift_listings.models.Person)
admin.site.register(gift_listings.models.Gift)
admin.site.register(gift_listings.models.ImportantDates)