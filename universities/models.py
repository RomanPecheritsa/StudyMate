from django.db import models
from django.utils.translation import gettext_lazy as _

from universities.enums import EducationFormType, WorkType


class University(models.Model):
    name = models.CharField(_("Название"), max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Университет")
        verbose_name_plural = _("Университеты")


class Speciality(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name="specialties",
        verbose_name=_("Университет"),
    )
    name = models.CharField(_("Название специальности"), max_length=100)

    def __str__(self):
        return f"{self.name} ({self.university})"

    class Meta:
        verbose_name = _("Специальность")
        verbose_name_plural = _("Специальности")


class SpecialityVersion(models.Model):
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name="versions",
        verbose_name=_("Специальность"),
    )
    year = models.PositiveIntegerField(_("Год поступления"))
    cost = models.PositiveIntegerField(_("Стоимость"))
    deadline = models.DateField(_("Дедлайн"))
    semesters_count = models.PositiveIntegerField(_("Количество семестров"))
    education_form_type = models.CharField(
        _("Форма обучения"),
        max_length=20,
        choices=EducationFormType.choices,
    )

    def __str__(self):
        return f"{self.speciality.name} ({self.year} г.)"

    class Meta:
        verbose_name = _("Версия специальности")
        verbose_name_plural = _("Версии специальностей")
        unique_together = ("speciality", "year")


class Semester(models.Model):
    speciality_version = models.ForeignKey(
        SpecialityVersion,
        on_delete=models.CASCADE,
        related_name="semesters",
        verbose_name=_("Версия специальности"),
    )
    number = models.PositiveIntegerField(_("Номер семестра"))
    cost = models.PositiveIntegerField(_("Стоимость"))
    deadline = models.DateField(_("Дедлайн"))

    def __str__(self):
        return f"Семестр {self.number} ({self.speciality_version})"

    class Meta:
        verbose_name = _("Семестр")
        verbose_name_plural = _("Семестры")


class Subject(models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="subjects",
        verbose_name=_("Семестр"),
    )
    name = models.CharField(_("Название предмета"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Предмет")
        verbose_name_plural = _("Предметы")


class Work(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="works",
        verbose_name=_("Предмет"),
    )
    title = models.CharField(_("Заголовок работы"), max_length=200)
    cost = models.PositiveIntegerField(_("Стоимость"))
    deadline = models.DateField(_("Дедлайн"))
    work_type = models.CharField(
        _("Тип работы"),
        max_length=30,
        choices=WorkType.choices,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Работа")
        verbose_name_plural = _("Работы")
