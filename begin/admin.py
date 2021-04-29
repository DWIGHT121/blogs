from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Articles)
# admin.site.register(ArticlesImage)

class ArticlesImageAdmin(admin.StackedInline):
    model = ArticlesImage

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = [ArticlesImageAdmin]

    class Meta:
       model = Articles

@admin.register(ArticlesImage)
class ArticlesImageAdmin(admin.ModelAdmin):
    pass