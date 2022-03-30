
from unicodedata import name
from flask import Blueprint, jsonify, abort, request
from ..models import Driver, db
import hashlib
import secrets

bp = Blueprint('Driver', __name__, url_prefix='/irxRaces')


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    user = Driver.query.all()  # ORM performs SELECT query
    result = []
    for t in user:
        result.append(t.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Driver.query.get_or_404(id)
    return jsonify(t.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3:
        return abort(400)
    if len(request.json['password']) < 8:
        return abort(400)

    # construct user
    t = Driver(
        username=request.json['username'],
        password=scramble(request.json['password'])
    )
    db.session.add(t)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(t.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Driver.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)