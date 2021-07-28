from django.utils.deprecation import MiddlewareMixin
from management.log.tasks import log_handler


class LogMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_response(self, request, response):
        log_handler(request, response)
        return response
