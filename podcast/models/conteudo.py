from django.db import models

# Create your models here.
from utils.mixins.models import SetUpModel


class ConteudoModel(SetUpModel):
    titulo = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'conteudo'
