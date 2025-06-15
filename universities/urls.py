from django.urls import path

from universities.views import HomePageView

app_name = "universities"

urlpatterns = [path("", HomePageView.as_view(), name="main")]
