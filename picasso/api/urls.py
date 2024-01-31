
from django.urls import path

from .views import CreateFileView, ListFilesView

app_name = 'api'

urlpatterns = [
    path('upload/', CreateFileView.as_view(), name='upload_file'),
    path('files/', ListFilesView.as_view(), name='list_files'),
]
