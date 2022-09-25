from django.contrib import admin
from .models import Order, About, Faq, Terms, Partners

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','flavour','size','order_status','size']
    list_filter=['placed_at','updated_at','order_status']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=['id','title','body','Author', 'created_on','updated_at']

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display=['id','title','body','Author', 'created_on','updated_at']

@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    list_display=['id','title','body','Author', 'created_on','updated_at']

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display=['id','title','body','Author','created_on','updated_at', 'picture']
