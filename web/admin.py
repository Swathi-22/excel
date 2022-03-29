from django.contrib import admin
from .models import Contact,Testimonial,Gallery,Update


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ( 'name','designation',)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary',)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'title',)