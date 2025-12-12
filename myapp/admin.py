from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('user', 'due_date')

admin.site.register(Task, TaskAdmin)
