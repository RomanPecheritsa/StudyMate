from django.contrib import admin

from universities.models import (
    University,
    Speciality,
    SpecialityVersion,
    Semester,
    Subject,
    Work,
)


class SemesterInline(admin.TabularInline):
    model = Semester
    extra = 1


class SpecialityVersionInline(admin.TabularInline):
    model = SpecialityVersion
    extra = 1


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("name", "university")
    list_filter = ("university",)
    search_fields = ("name",)
    autocomplete_fields = ["university"]
    inlines = [SpecialityVersionInline]


@admin.register(SpecialityVersion)
class SpecialityVersionAdmin(admin.ModelAdmin):
    list_display = (
        "speciality",
        "year",
        "cost",
        "deadline",
        "semesters_count",
        "education_form_type",
    )
    list_filter = ("speciality", "year")
    search_fields = ("speciality__name",)
    autocomplete_fields = ["speciality"]
    inlines = [SemesterInline]


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("number", "speciality_version", "cost", "deadline")
    list_filter = ("speciality_version",)
    autocomplete_fields = ["speciality_version"]
    inlines = [SubjectInline]
    search_fields = ["speciality_version__speciality__name", "number"]


class WorkInline(admin.TabularInline):
    model = Work
    extra = 1


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "semester")
    list_filter = ("semester",)
    autocomplete_fields = ["semester"]
    inlines = [WorkInline]
    search_fields = ["name", "semester__number"]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "work_type", "cost", "deadline")
    list_filter = ("work_type", "subject")
    autocomplete_fields = ["subject"]
    search_fields = ("title",)
