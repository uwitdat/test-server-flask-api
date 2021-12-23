from flask import Blueprint
from testserver.database.models.Service import Service
from testserver.database.models.Provider import Provider
from testserver.endpoints.providers.schemas import provider_schema
from testserver.database import db_session
from flask import request, jsonify
from .schemas import service_schema, services_schema


bp = Blueprint('services', __name__)


@bp.route('/providers/<id>/add-service', methods=['POST'])
def new_service(id):
    name = request.json['name']
    description = request.json['description']

    provider = db_session.query(Provider).filter_by(id=id).first()

    new_service = Service(
        name=name, description=description, provided_by=provider)

    db_session.add(new_service)
    try:
        db_session.commit()
        return service_schema.dumps(new_service)
    except:
        db_session.rollback()
        raise

@bp.route('/providers/<id>/services', methods=['GET'])
def get_all_services_from_provider(id):
    provider = db_session.query(Provider).filter_by(id=id).first()

    if not provider:
        return jsonify({'Message': f'Provider with id: {id} does not exist', 'Status': 404})

    services = db_session.query(Service).filter(provider.id == Service.provider_id).all()
    result = services_schema.dump(services)
    return jsonify(result)

@bp.route('/services/<id>/provider', methods=['GET'])
def get_provider_from_service(id):
    service =  db_session.query(Service).filter_by(id=id).first()

    if not service:
        return jsonify({'Message': f'Service with id: {id} does not exist', 'Status': 404})
    
    provider = db_session.query(Provider).filter(Provider.id == service.provider_id).first()
    result = provider_schema.dump(provider)
    return jsonify(result)

