from django.conf.urls import url
from . import views

urlpatterns = [
    url("^events/(?P<pk>\d+)/$", views.show_questioning_session),
    url("^events/(?P<pk>\d+)/ajax$", views.handle_questioning_ajax, name="handle_questioning_ajax"),
]
