from django.contrib import admin
from .models import Products ,Offer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
  
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')
  

admin.site.register(Products,ProductAdmin) ## pass Products class as argument
admin.site.register(Offer,OfferAdmin)