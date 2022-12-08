import http

from exceptions.application import ApplicationException


class BadRequestException(ApplicationException):
    status_code = http.HTTPStatus.BAD_REQUEST
    detail = "Bad request"
