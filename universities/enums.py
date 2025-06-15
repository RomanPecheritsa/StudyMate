from django.db.models import TextChoices


class EducationFormType(TextChoices):
    FULL_TIME = "очная", "Очная"
    PART_TIME = "заочная", "Заочная"


class WorkType(TextChoices):
    ESSAY = "эссе", "Эссе"
    TEST = "контрольная", "Контрольная работа"
    REPORT = "реферат", "Реферат"
    COURSEWORK = "курсовая", "Курсовая работа"
    COURSE_PROJECT = "курсовой проект", "Курсовой проект"
    THESIS = "ВКР", "Выпускная квалификационная работа"
