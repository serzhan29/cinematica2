from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Rating, Actor, RatingStar, Reviews, Movie, MovieShots


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name")
    list_display_links = ("name", )
admin.site.register(Category, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft", "id")
    list_filter = ("category", "year", )
    search_fields = ("title",)
    save_on_top = True
    save_as = True


class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Actor, ActorAdmin)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(MovieShots)
admin.site.register(Movie, MovieAdmin)


