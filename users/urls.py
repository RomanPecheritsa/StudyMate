from django.urls import path
from users.views import TelegramCreateUserView, confirm_email, LoginView

urlpatterns = [
    path(
        "api/telegram/create_user/",
        TelegramCreateUserView.as_view(),
        name="telegram_create_user",
    ),
    path("users/email-confirm/<uuid:token>/", confirm_email, name="confirm_email"),
    path("login/", LoginView.as_view(), name="login"),
]
