from django.conf.urls import url
from . import views

app_name = 'wlmaps'
urlpatterns = [
    url(r'', views.default_map, name="default"),
]
