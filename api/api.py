from flask import Blueprint, jsonify, abort, request
from utils import get_posts_all, get_post_by_pk
import logging

api = Blueprint('api', __name__)

logger = logging.getLogger('api')
logger.setLevel(logging.INFO)
file_log = logging.FileHandler('logs/api.log', encoding='utf-8')  # файл записи логов
file_log.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))  # формат логов
logger.addHandler(file_log)


@api.route('/api/posts')
def get_posts():
    """Возвращает список постов в виде JSON-списка"""
    posts = get_posts_all()
    logger.info('Выполнен запрос /api/posts')
    return jsonify(posts)


@api.route('/api/posts/')
def get_post_id():
    """Возвращает пост в виде JSON-словаря"""
    s = request.args.get('s')
    post = get_post_by_pk(s)
    if post == ValueError:
        logger.error(f'Данных по запросу /api/posts/?s={s} не существет')
        abort(404)
    logger.info(f'Запрос /api/posts/?s={s} выполнен успешно')
    return jsonify(post)
