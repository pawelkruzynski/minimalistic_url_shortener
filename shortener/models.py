import uuid

from django.db import models


class Shortener(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, unique=True, editable=False)
    url = models.URLField("URL", unique=True)
