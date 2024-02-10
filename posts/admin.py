from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.car_model)


class brand_model_Admin(admin.ModelAdmin):
    prepopulated_fields={'slug':('brand_name',)}
    list_display = ['brand_name', 'slug']
admin.site.register(models.brand_model,brand_model_Admin)


admin.site.register(models.comments_Model)
admin.site.register(models.purchase)

