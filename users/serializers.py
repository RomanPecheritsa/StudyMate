# serializers.py

from rest_framework import serializers
from .models import User
import uuid
import secrets
import string


def generate_random_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


class EmailOnlyUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        email = validated_data["email"]

        request = self.context.get("request")
        if not request:
            raise serializers.ValidationError("Request не передан")

        current_host = request.META["HTTP_HOST"]

        password = generate_random_password()
        auth_token = uuid.uuid4()

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "is_active": False,
                "auth_token": auth_token,
            },
        )

        if not created:
            user.auth_token = auth_token
            user.save(update_fields=["auth_token"])

        user.set_password(password)
        user.save()

        url = f"http://{current_host}/users/email-confirm/{auth_token}"

        from users.utils import send_email_confirm

        send_email_confirm(url, user)

        return user
