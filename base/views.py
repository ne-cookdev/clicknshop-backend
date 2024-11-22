import json
import time

import jwt
import logging.config

from decouple import config
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from base.serializers import IndexSerializer

logger = logging.getLogger(__name__)


class IndexAPIView(APIView):
    """
    Эндпоинт открытия курса.
    """
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        """
        Метод берет только курсы, номера которых передали в параметре get-запроса.
        """
        return Response(data="Server Started", status=status.HTTP_200_OK)
