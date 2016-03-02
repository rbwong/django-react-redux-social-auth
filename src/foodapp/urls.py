# django
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

# app
from base import views as base_views

# rest_framework
from rest_framework_nested import routers

# views
from posts.views import (
    PostViewSet,
    CollectionViewSet,
    PostCollectorView,
    PostUnCollectorView,
)
from users.views import AccountViewSet, UserView
from base import views as base_views


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', AccountViewSet)
router.register(r'posts', PostViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    # posts
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/posts/(?P<post_pk>[0-9]+)/collect', PostCollectorView.as_view()),
    url(r'^api/v1/posts/(?P<post_pk>[0-9]+)/uncollect', PostUnCollectorView.as_view()),
    # accounts
    url(r'^api/v1/me', UserView.as_view()),
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # users
    url(r'^', include('users.urls')),
    # app
    url(r'^api/v1/getdata', base_views.ProtectedDataView.as_view(), name='protected_data'),
    url(r'', cache_page(settings.PAGE_CACHE_SECONDS)(base_views.IndexView.as_view()), name='index'),
]
