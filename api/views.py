import os

from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class HostInfoSerializer(serializers.Serializer):
    region = serializers.CharField()
    public_host = serializers.CharField()
    availability_zone = serializers.CharField()


class IndexView(APIView):
    def get(self, request):
        return Response(
            HostInfoSerializer(
                instance={
                    "region": settings.EC2_REGION,
                    "public_host": settings.EC2_PUBLIC_HOSTNAME,
                    "availability_zone": settings.EC2_AVAILABILITY_ZONE,
                }
            ).data
        )