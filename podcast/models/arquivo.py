from django.db import models

# Create your models here.
from utils.mixins.models import SetUpModel


class ArquivoModel(SetUpModel):
    url = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = "arquivo"
