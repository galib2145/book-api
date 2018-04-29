from django.conf.urls import url

from .views import LoginView, ExampleView

urlpatterns = [
    url(r'^login/?$', LoginView.as_view()),
    url(r'^ex/?$', ExampleView.as_view()),
]