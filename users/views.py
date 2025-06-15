from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.forms import ConfirmRegistrationForm, LoginForm
from users.models import User
from users.serializers import EmailOnlyUserSerializer


class TelegramCreateUserView(APIView):
    def post(self, request):
        serializer = EmailOnlyUserSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "email": user.email,
                    "message": "Пользователь создан. Письмо отправлено.",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def confirm_email(request, token):
    user = User.objects.filter(auth_token=token).first()

    if not user:
        return render(
            request, "confirm_error.html", {"error": "Неверный или истёкший токен"}
        )

    if request.method == "POST":
        form = ConfirmRegistrationForm(request.POST)

        if form.is_valid():
            user.first_name = form.cleaned_data["first_name"]
            user.set_password(form.cleaned_data["password1"])
            user.is_active = True
            user.auth_token = None
            user.save()

            login(request, user)
            return redirect(reverse("login"))

    else:
        form = ConfirmRegistrationForm()

    return render(request, "confirm_registration.html", {"form": form})


class LoginView(generic.FormView):
    template_name = "login.html"
    success_url = reverse_lazy("universities:main")
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=email, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect(f"{self.request.path}?error=1")
