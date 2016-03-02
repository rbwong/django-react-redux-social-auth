from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User
from .permissions import IsAccountOwner
from .serializers import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (
            IsAuthenticated(),
            IsAccountOwner()
        )


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        return (
            IsAuthenticated(),
            IsAccountOwner()
        )

    def retrieve(self, request):
        return Response(UserSerializer(request.user).data)
