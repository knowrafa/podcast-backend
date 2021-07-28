from django.conf import settings
from django.db import models

from authentication.choices import PermissionChoices
from utils.mixins.models import SetUpModel


class Permission(SetUpModel):
    """
    Base permission model.
    Define you own relation with other models.
    - Exemplos:
        1. company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='permissoes')
        2. bank = models.ForeignKey('Bank', on_delete=models.CASCADE, related_name='permissoes')
    """
    acess = models.CharField(max_length=20, choices=PermissionChoices.acess())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='permissions')
    acess_level = models.CharField(max_length=20, choices=PermissionChoices.acess_level(), null=True, blank=True)

    class Meta:
        db_table = 'permission'
        verbose_name = 'permission'
        verbose_name_plural = 'permissions'
        unique_together = ('acess', 'user', 'acess_level')
