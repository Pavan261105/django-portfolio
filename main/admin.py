from django.contrib import admin

# Register your models here.
from .models import Project, Contact, Blog, Experience
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Experience)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
