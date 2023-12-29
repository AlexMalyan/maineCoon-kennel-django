from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bitrh', 'get_html_image')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('name', 'cattery')
    fields = ('name', 'cattery', 'gender', 'merits', 'bitrh', 'description',
              'image', 'get_html_image')
    readonly_fields = ('get_html_image',)

    def get_html_image(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=50")

    get_html_image.short_description = "Фото"


admin.site.register(Cat, CatAdmin)

admin.site.site_title = 'Админка ШатоДеКун'
admin.site.site_header = 'Админ - панель питомника ШатоДеКун'
