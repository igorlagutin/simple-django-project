import os

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request):
        return Response({"data": f"host: {settings.HOST_INFO}"})