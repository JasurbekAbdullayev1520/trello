from django.contrib import admin
from .models import Task, Attechment, SubTask, Category

admin.site.register(Task)
admin.site.register(Attechment)
admin.site.register(SubTask)
admin.site.register(Category)
