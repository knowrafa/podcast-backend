from auditlog.mixins import LogEntryAdminMixin
from auditlog.models import LogEntry
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import LogModel


@admin.register(LogModel)
class LogAdmin(admin.ModelAdmin):
    list_display = ['user', 'nome', 'method', 'response_status_code', 'criado_em', 'modificado_em']

    list_filter = ('user',)
    readonly_fields = (
        'headers_tag',
        'meta_tag',
        'request_body_tag',
        'response_body_tag',
        'criado_em',
        'modificado_em',
        'method',
        'user',
        'nome',
        'headers',
        'meta',
        'response_body',
        'request_body',
        'user_agent',
        'dispositivo',
        'response_status_code',
    )

    fieldsets = (
        (None, {'fields': (('user', 'nome'), ('user_agent', 'dispositivo'),)}),
        (_('Status'), {
            'fields': (('method', 'response_status_code'),),
        }),
        (_('Meta'), {'fields': (('meta_tag', 'meta'),)}),
        (_('Headers'), {'fields': (('headers_tag', 'headers'),)}),
        (_('Request'), {
            'fields': ('request_body_tag', 'request_body',),
        }),
        (_('Response'), {
            'fields': ('response_body_tag', 'response_body',),
        }),
        (_('Errors'), {
            'fields': ('error_response_log', 'error_user_agent',),
        }),
        (_('Important dates'), {'fields': (('criado_em', 'modificado_em'),)}),
    )


class LogEntryAdmin(admin.ModelAdmin, LogEntryAdminMixin):
    list_display = ['created', 'resource_url', 'action', 'changes', 'user_url']
    search_fields = ['timestamp', 'object_repr', 'changes', 'actor__first_name', 'actor__last_name']
    readonly_fields = ['created', 'resource_url', 'action', 'user_url', 'msg', 'changes', ]
    fieldsets = [
        (None, {'fields': ['created', 'user_url', 'resource_url']}),
        ('Changes', {'fields': ['action', 'msg', 'changes']}),
    ]


admin.site.unregister(LogEntry)
admin.site.register(LogEntry, LogEntryAdmin)
