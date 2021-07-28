import json

from celery import shared_task

from authentication.user.models import User
from .api.v1.serializers import LogSerializer


def log_handler(request, response):
    try:
        meta = {}
        buff = dict(request.META)
        buff.pop('werkzeug.request', None)
        buff.pop('wsgi.input', None)
        buff.pop('wsgi.errors', None)
        buff.pop('wsgi.file_wrapper', None)
        for key, value in buff.items():
            if isinstance(value, bytes):
                meta[key] = value.decode('utf-8')
            elif isinstance(value, (list, tuple, bool, dict, str)):
                meta[key] = value

    except Exception as e:
        meta = {"meta_log_err": repr(e)}

    payload_log = {
        "user": str(request.user.pk) if request.user else '',
    }

    try:
        payload_log = {
            **payload_log,
            "path": request.path,
            "content_type": request.content_type,
            "method": request.method,
            "nome": str(request.user) if isinstance(request.user, User) else '',
            "meta": meta,
            "headers": dict(request.headers),
            "response_status_code": int(response.status_code),
        }

    except Exception as e:
        payload_log['error_request_log'] = repr(e)

    try:
        payload_log['request_body'] = json.loads(request.body.decode("UTF-8")) if request.body else {}
    except (SyntaxError, KeyError, Exception):
        try:
            payload_log['request_body'] = request.body.decode("UTF-8") if request.body else {}
        except Exception as e:
            payload_log['error_request_body'] = repr(e)

    try:
        payload_log['method'] = request.method

    except Exception as e:
        payload_log['error_acao_log'] = repr(e)

    try:
        user_agent_str = 'other'
        if request.user_agent:
            agent = request.user_agent
            if agent.is_pc:
                user_agent_str = 'browser'
            elif agent.is_mobile:
                user_agent_str = 'mobile'
            elif agent.is_bot:
                user_agent_str = 'bot'
            elif agent.is_tablet:
                user_agent_str = 'tablet'
            elif agent.is_email_client:
                user_agent_str = 'email'
            elif agent.is_touch_capable:
                user_agent_str = 'touch_capable'

        payload_log['user_agent'] = str(request.user_agent)
        payload_log['dispositivo'] = user_agent_str

    except Exception as e:
        payload_log['error_user_agent'] = repr(e)

    try:
        payload_log['response_body'] = json.loads(response.content.decode("UTF-8")) if response.content else {}
    except (SyntaxError, KeyError, Exception):
        try:
            payload_log['response_body'] = response.content.decode("UTF-8") if response.content else {}
        except Exception as e:
            payload_log['error_response_log'] = repr(e)

    salvar_log.apply_async(args=(payload_log,))


@shared_task(exchange='podcast', routing_key='podcast.log')
def salvar_log(payload_log):
    log = LogSerializer(data=payload_log)
    log.is_valid(raise_exception=True)
    log.save()
    print('Log Salvo!')
