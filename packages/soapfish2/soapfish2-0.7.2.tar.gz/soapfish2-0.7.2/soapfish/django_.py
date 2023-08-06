import logging
import os
from .core import SOAPRequest
from .soap_dispatch import SOAPDispatcher
logger = logging.getLogger('soapfish')

__all__ = ['django_dispatcher']


class DjangoEnvironWrapper:
    def __init__(self, environ):
        self.environ = environ

    def get(self, name, default=None):
        name = name.replace('-', '_').upper()
        for key in (name, 'HTTP_' + name):
            if key in self.environ:
                return self.environ[key]
        return default


def django_dispatcher(service, **dispatcher_kwargs):
    from django.http import HttpResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.utils.timezone import now

    def log_request(byte_content, prefix, now):
        if os.getenv('SOAPFISH_REQUEST_LOG', 'false').lower() == 'true':
            log_path = os.getenv('SOAPFISH_REQUEST_LOG_PATH', '/tmp/logs/')
            name = log_path +prefix+ now.isoformat()
            with open(name, "wb") as arch:
                arch.write(byte_content)
    def django_dispatch(request):
        nowname = now()
        log_request(request.body, "request_", nowname)
        soap_request = SOAPRequest(DjangoEnvironWrapper(request.environ), request.body)
        soap_request._original_request = request
        logger.debug(request.body)
        soap_dispatcher = SOAPDispatcher(service, **dispatcher_kwargs)
        soap_response = soap_dispatcher.dispatch(soap_request)
        log_request(soap_response.http_content, "response_", nowname)
        response = HttpResponse(soap_response.http_content)
        logger.debug(soap_response.http_content)
        response.status_code = soap_response.http_status_code
        if response.status_code >=300:
            logger.error("Response with error %s %s", response.status_code, soap_response.http_content)
        for k, v in soap_response.http_headers.items():
            response[k] = v
        return response

    return csrf_exempt(django_dispatch)
