from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, RetrieveAPIView
)

from .models import Picture
from .serializers import PictureSerializer, ColorSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from PIL import Image


class PicturePostView(CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class ColorRetrieveView(RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = ColorSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, *args, **kwargs):
        img = Image.open(**kwargs)
        colors = img.getcolors(256)  # put a higher value if there are many colors in your image
        max_occurence, most_present = 0, 0
        try:
            for c in colors:
                if c[0] > max_occurence:
                    (max_occurence, most_present) = c
            return most_present
        except TypeError:
            raise Exception("Too many colors in the image")


class PictureDeleteView(DestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
