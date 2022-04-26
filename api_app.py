from flask import Blueprint, jsonify, abort
from utils import get_posts_all, get_post_by_pk
import logging

api = Blueprint('api', __name__)

logger = logging.getLogger('api')
logger.setLevel(logging.INFO)
file_log = logging.FileHandler('logs/api.log', encoding='utf-8')  # файл записи логов
file_log.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))  # формат логов
logger.addHandler(file_log)


@api.route('/api/posts', methods=['GET'])
def get_posts():
    """Возвращает список постов в виде JSON-списка"""
    logger.info('Запрос /api/posts')
    return jsonify(get_posts_all()), 200


@api.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post_id(post_id):
    """Возвращает пост в виде JSON-словаря"""
    logger.info(f'Запрос /api/posts/{post_id}')
    post = get_post_by_pk(post_id)
    if post == ValueError:
        abort(404)
    return jsonify(get_post_by_pk(post_id))