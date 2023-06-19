from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Rating, Actor, RatingStar, Movie


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name")
    list_display_links = ("name", )
admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft", "id")
    list_filter = ("category", "year", )
    search_fields = ("title",)
admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)
    search_fields = ("name",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Actor, ActorAdmin)
admin.site.register(RatingStar)





