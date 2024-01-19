from django.contrib import admin
from django.db import models
from .models import *

MODELS = [Individual_Pricing, Business_Pricing]

for MODEL in MODELS:

    @admin.register(MODEL)
    class ModelAdmin(admin.ModelAdmin):
        list_display = [field.name for field in MODEL._meta.get_fields()]
