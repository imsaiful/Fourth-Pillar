from django.contrib import admin
from .models import Republic, Ndtv, Indiatoday


class RepublicModalAdmin(admin.ModelAdmin):
    list_display = ["headline", "date", "category", "sentiment"]

    class Meta:
        model = Republic


class NdtvModalAdmin(admin.ModelAdmin):
    list_display = ["headline", "date", "category", "sentiment"]

    class Meta:
        model = Ndtv


class IndiatodayModalAdmin(admin.ModelAdmin):
    list_display = ["headline", "date", "category", "sentiment"]

    class Meta:
        model = Indiatoday


admin.site.register(Republic, RepublicModalAdmin)
admin.site.register(Ndtv, NdtvModalAdmin)
admin.site.register(Indiatoday, IndiatodayModalAdmin)

# Register your models here.
