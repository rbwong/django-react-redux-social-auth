import os

# django
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

# rest_framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class IndexView(View):
    """Render main page."""

    def get(self, request):
        """Return html for main application page."""

        abspath = open(os.path.join(settings.SITE_ROOT, 'static_dist/index.html'), 'r')
        return HttpResponse(content=abspath.read())


class ProtectedDataView(GenericAPIView):
    """Return protected data  main page."""

    authentication_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """Process GET request and return protected data."""

        data = {
            'data': 'THIS IS THE PROTECTED STRING FROM SERVER',
        }

        return Response(data, status=status.HTTP_200_OK)