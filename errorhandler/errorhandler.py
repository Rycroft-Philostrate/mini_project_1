from flask import Blueprint


err = Blueprint('err', __name__)


@err.errorhandler(400)
def error_400(error):
    return 'Некорректный запрос!', 400


@err.app_errorhandler(404)
def error_404(error):
    return 'Данных по такому запросу не существует!', 404


@err.app_errorhandler(500)
def error_500(error):
    return 'Внутренняя ошибка сервера!', 500
