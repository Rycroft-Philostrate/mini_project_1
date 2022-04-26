from flask import Blueprint


err = Blueprint('err', __name__)


@err.app_errorhandler(404)
def error_404(e):
    return 'Статус-код 404'


@err.app_errorhandler(500)
def error_500(e):
    return 'Статус-код 500'
