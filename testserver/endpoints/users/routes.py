from flask import Blueprint
from testserver.database.models.User import User
from testserver.database import db_session
from flask import request, jsonify
from .schemas import user_schema, users_schema


bp = Blueprint('users', __name__)


@bp.route('/users', methods=['POST'])
def new_user():
    name = request.json['name']
    email = request.json['email']

    new_user = User(name=name, email=email)

    db_session.add(new_user)
    try:
        db_session.commit()
        return user_schema.dumps(new_user)
    except:
        db_session.rollback()
        raise


@bp.route('/users', methods=['GET'])
def get_all_users():
    all_users = db_session.query(User).all()
    result = users_schema.dump(all_users)
    return jsonify(result)


@bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = db_session.query(User).get(id)
    db_session.delete(user)
    db_session.commit()
    return f'user with id: {id} deleted successfuly'
