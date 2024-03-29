from django.db import models


class File(models.Model):
    """
    Модель File
    """
    file = models.FileField(upload_to='./files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
