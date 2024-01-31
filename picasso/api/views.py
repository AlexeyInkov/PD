from rest_framework.generics import CreateAPIView

from .models import File
from .serializer import FileSerializer


class UploadFileView(CreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
