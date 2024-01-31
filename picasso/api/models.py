from django.db import models


class File(models.Model):
    """
    Модель File
    """
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
