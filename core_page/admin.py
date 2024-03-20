from django.contrib import admin
from .models import BlogItems, BlogCategory, BackCategory, Subscriber

# Register your models here.

admin.site.register(BlogCategory)
admin.site.register(BlogItems)
admin.site.register(BackCategory)
admin.site.register(Subscriber)
