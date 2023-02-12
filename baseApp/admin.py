from django.contrib import admin

from .models import TodoTable

db = [TodoTable]

admin.site.register(db)

