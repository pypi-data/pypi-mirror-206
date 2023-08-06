from flask_restx import Resource
from server.api import api
from server.database.models import Permission
from .serializers import permission_serializer
from .form import form_permission_update

np_permission = api.namespace(
    'permissions',
    description='Operações relacionadas a permissões',
    path='/v1/permissions'
)


class PermissionResource(Resource):
    @np_permission.marshal_with(permission_serializer)
    def get(self, id=None):
        """Retorna a permissão"""
        if id:
            return Permission.query.get_or_404(str(id))
        else:
            return Permission.query.all()

    @np_permission.marshal_with(permission_serializer)
    @np_permission.expect(form_permission_update)
    def put(self, id):
        """Define se a permissão está ativa ou não"""
        data = form_permission_update.parse_args()
        permission = Permission.query.get_or_404(str(id))
        permission.update(**data)
        permission.save()
        return permission


np_permission.add_resource(
    PermissionResource, '/',
    endpoint='permission',
    methods=['GET']
)

np_permission.add_resource(
    PermissionResource, '/<uuid:id>',
    endpoint='permission-id',
    methods=['GET', 'PUT']
)
