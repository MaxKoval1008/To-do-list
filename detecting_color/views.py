from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, RetrieveAPIView
)
from rest_framework.views import APIView

from .models import Picture
from .serializers import PictureSerializer, ColorSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from PIL import Image


class PicturePostView(CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class ColorRetrieveView(APIView):
    def get(self, request, pk):
        picture_img = Picture.objects.get(id=pk)
        serializer_class = PictureSerializer(picture_img)
        return Response(serializer_class.data)


class PictureDeleteView(DestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
