from django.conf.urls import url, include
from rest_framework import routers

import books.views as views
from auth import urls as auth_urls

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    )),
    url(r'^auth/', include(auth_urls)),

]
