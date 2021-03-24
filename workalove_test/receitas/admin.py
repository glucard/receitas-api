from django.contrib import admin

from .models import Receita, Chef

admin.site.register([Receita, Chef])