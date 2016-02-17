from django.conf.urls import url, include
from django.contrib import admin

# rest_framework
from rest_framework_nested import routers

# views
from posts.views import PostViewSet, CollectionViewSet
from users.views import AccountViewSet, UserView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('users.urls')),
]

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', AccountViewSet)
router.register(r'posts', PostViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    # api
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/me', UserView.as_view()),
    # admin
    url(r'^admin/', include(admin.site.urls)),
]
