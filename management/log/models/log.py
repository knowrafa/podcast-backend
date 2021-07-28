from django.conf import settings
from django.db import models

from utils.mixins.models import SetUpModel
from django.utils.translation import ugettext_lazy as _

from utils.templates.html_table import table_template


class LogModel(SetUpModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='logs',
                             null=True, blank=True)

    nome = models.CharField(max_length=255, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    error_request_log = models.TextField(null=True, blank=True)
    error_request_body = models.TextField(null=True, blank=True)

    meta = models.JSONField(verbose_name=_('meta'), null=True, blank=True)
    headers = models.JSONField(verbose_name=_('headers'), null=True, blank=True)
    request_body = models.JSONField(verbose_name=_('request_body'), null=True, blank=True)
    response_body = models.JSONField(verbose_name=_('response_body'), null=True, blank=True)
    response_status_code = models.IntegerField(verbose_name=_('response_status_code'), null=True, blank=True)

    error_acao_log = models.TextField(null=True, blank=True)

    user_agent = models.TextField(blank=True, null=True)

    dispositivo = models.CharField(max_length=255, blank=True, null=True)

    error_user_agent = models.TextField(blank=True, null=True)

    error_response_log = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log'
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def headers_tag(self):
        return table_template(self.headers)

    def meta_tag(self):
        return table_template(self.meta)

    def request_body_tag(self):
        return table_template(self.request_body)

    def response_body_tag(self):
        return table_template(self.response_body)
