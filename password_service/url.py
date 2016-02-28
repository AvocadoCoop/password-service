from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.password_service, name="password_service"),
]
