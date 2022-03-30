from unicodedata import name
from flask import Blueprint, jsonify, abort, request
from ..models import Races, db
import hashlib
import secrets



def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('races', __name__, url_prefix='/races')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    races = Races.query.all()  # ORM performs SELECT query
    result = []
    for t in races:
        result.append(t.serialize())  # build list of Races as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    t = Races.query.get_or_404(id)
    return jsonify(t.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'starting_position' not in request.json and 'ending_position' not in request.json and 'qualifying_time' not in request.json and 'average_lap_times' not in request.json and 'best_lap_time' not in request.json:
        return abort(400)

    # construct user
    t = Races(
        starting_position=request.json['starting_position'],
        ending_position=request.json['ending_position'],
        qualifying_time=request.json['qualifying_time'],
        average_lap_times=request.json['average_lap_times'],
        best_lap_time=request.json['best_lap_time']
    )
    db.session.add(t)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(t.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    t = Races.query.get_or_404(id)
    try:
        db.session.delete(t)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
