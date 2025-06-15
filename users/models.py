from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    ROLE_CHOICES = (
        ("user", "Пользователь"),
        ("expert", "Эксперт"),
        ("admin", "Администратор"),
    )

    username = None
    email = models.EmailField(
        verbose_name="Email", unique=True, help_text="Основное поле для входа"
    )
    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=True)
    role = models.CharField(
        verbose_name="Роль", max_length=10, choices=ROLE_CHOICES, default="user"
    )
    telegram_id = models.BigIntegerField(
        verbose_name="Telegram ID", unique=True, null=True, blank=True
    )
    is_staff = models.BooleanField(verbose_name="Сотрудник", default=False)
    is_active = models.BooleanField(verbose_name="Активен", default=False)
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации", auto_now_add=True
    )
    auth_token = models.UUIDField(
        verbose_name="Токен подтверждения",
        default=uuid.uuid4,
        null=True,
        blank=True,
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email or f"ID {self.id}"

    @property
    def is_user(self):
        return self.role == "user"

    @property
    def is_expert(self):
        return self.role == "expert"

    @property
    def is_admin(self):
        return self.role == "admin"
