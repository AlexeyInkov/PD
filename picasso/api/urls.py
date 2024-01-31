
from django.urls import path

from .views import UploadFileView

app_name = 'api'

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload_file'),
]
