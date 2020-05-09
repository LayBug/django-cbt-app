from django.contrib import admin
from . import models

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('course_name',)}


admin.site.register(models.Subject,SubjectAdmin)
admin.site.register(models.QA)
admin.site.register(models.Score)
