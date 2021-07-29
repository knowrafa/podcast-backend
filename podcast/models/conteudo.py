from django.db import models

# Create your models here.
from utils.mixins.models import SetUpModel


class ConteudoModel(SetUpModel):
    id_conteudo = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    members = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.URLField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(null=True)
    file = models.OneToOneField(
        "ArquivoModel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "conteudo"
