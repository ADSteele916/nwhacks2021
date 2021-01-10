from django.contrib import admin

from .models import Course, Bin, Assessment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    pass


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    pass
