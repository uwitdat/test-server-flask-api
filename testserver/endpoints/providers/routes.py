from flask import Blueprint
from testserver.database.models.Provider import Provider
from testserver.database import db_session
from flask import request, jsonify
from .schemas import provider_schema, providers_schema


bp = Blueprint('providers', __name__)


@bp.route('/providers', methods=['POST'])
def new_provider():
    name = request.json['name']
    description = request.json['description']

    new_provider = Provider(name=name, description=description)

    db_session.add(new_provider)
    try:
        db_session.commit()
        return provider_schema.dumps(new_provider)
    except:
        db_session.rollback()
        raise


@bp.route('/providers', methods=['GET'])
def get_all_providers():
    all_providers = db_session.query(Provider).all()
    result = providers_schema.dump(all_providers)
    return jsonify(result)


@bp.route('/providers/<id>', methods=['DELETE'])
def delete_provider(id):
    provider = db_session.query(Provider).get(id)
    db_session.delete(provider)
    db_session.commit()
    return f'provider with id: {id} deleted successfuly'
