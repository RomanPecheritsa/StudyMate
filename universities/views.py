from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = "base.html"
