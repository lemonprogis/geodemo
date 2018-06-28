from django.conf.urls import url

from views import get_world_borders

urlpatterns = [
    url(r'^world-borders/$',get_world_borders),
]