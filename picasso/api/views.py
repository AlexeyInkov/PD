from rest_framework.generics import CreateAPIView, ListAPIView

from .models import File
from .serializer import FileSerializer


class CreateFileView(CreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def post(self, request, *args, **kwargs):
        file = self.create(request, *args, **kwargs)
        #  celery
        return file


class ListFilesView(ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
