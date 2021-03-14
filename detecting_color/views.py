from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, RetrieveAPIView
)
from .models import Picture
from .serializers import PictureSerializer


class PicturePostView(CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class ColorRetrieveView(RetrieveAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PictureDeleteView(DestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

