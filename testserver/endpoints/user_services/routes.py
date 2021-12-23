from flask import Blueprint
from testserver.database.models.Service import Service
from testserver.database.models.User import User
from testserver.database.models.UserService import UserService
from testserver.endpoints.providers.schemas import provider_schema
from testserver.endpoints.services.schemas import services_schema
from testserver.database import db_session
from flask import request, jsonify
from .schemas import user_service_schema, user_services_schema


bp = Blueprint('user_services', __name__)

@bp.route('/userservices', methods=['GET'])
def get_all_user_services():
    all_user_services = db_session.query(UserService).all()
    result = user_services_schema.dump(all_user_services)
    return jsonify(result)

@bp.route('/user/<userid>/add-service/<serviceid>', methods=['POST'])
def add_service_to_user(userid, serviceid):

    user = db_session.query(User).filter(User.id == userid).first()
    service = db_session.query(Service).filter(Service.id == serviceid).first()

    if not user:
        return jsonify({'Message': f'User with id: {userid} does not exist', 'Status': 404})

    if not service:
        return jsonify({'Message': f'Service with id: {serviceid} does not exist', 'Status': 404})

    new_user_service = UserService(used_by = user, service = service)

    db_session.add(new_user_service)
    try:
        db_session.commit()
        return user_service_schema.dumps(new_user_service)
    except:
        db_session.rollback()
        raise


@bp.route('/user/<id>/services', methods=['GET'])
def get_services_from_user(id):
    user = db_session.query(User).filter(id == User.id).first()

    if not user:
        return jsonify({'Message': f'User with id: {id} does not exist', 'Status': 404})

    user_services = db_session.query(UserService).filter(user.id == UserService.user_id).all()
    result = user_services_schema.dump(user_services)

    for service in result:
        services = db_session.query(Service).filter(service['service_id'] == Service.id).all()
        return services_schema.dumps(services)