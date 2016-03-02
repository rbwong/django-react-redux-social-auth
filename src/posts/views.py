# rest_framework
from rest_framework import permissions, viewsets, generics

# models
from .models import Post, Collection

# permissions
from .permissions import (
    IsOwnerOfPost,
    IsOwnerOfCollection
)

# serializers
from .serializers import (
    PostSerializer,
    CollectionSerializer,
    PostCollectorSerializer,
    PostUnCollectorSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 50

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        return (IsOwnerOfPost(), )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        return super(PostViewSet, self).perform_create(serializer)


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 50

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        if self.request.method == 'PUT':
            return (permissions.IsAuthenticated(),)

        return (IsOwnerOfCollection(), )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        return super(CollectionViewSet, self).perform_create(serializer)


class PostCollectorView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCollectorSerializer
    lookup_url_kwarg = "post_pk"

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.IsAuthenticated(),)

    def get_queryset(self):
        post_pk = self.kwargs.get(self.lookup_url_kwarg)
        queryset = self.queryset.filter(pk=post_pk)
        return queryset


class PostUnCollectorView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUnCollectorSerializer
    lookup_url_kwarg = "post_pk"

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.IsAuthenticated(),)

    def get_queryset(self):
        post_pk = self.kwargs.get(self.lookup_url_kwarg)
        queryset = self.queryset.filter(pk=post_pk)
        return queryset
