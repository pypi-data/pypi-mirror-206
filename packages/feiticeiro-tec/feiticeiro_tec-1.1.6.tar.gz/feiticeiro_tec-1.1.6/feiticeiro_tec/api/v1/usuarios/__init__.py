from flask_restx import Resource
from server.api import api
from server.database.models import Usuario
from .forms import usuario_form
from .serializers import usuario_serializer

np_usuario = api.namespace(
    'usuarios',
    description='Operações relacionadas a usuários',
    path='/v1/usuarios'
)


class UsuarioResource(Resource):

    @np_usuario.expect(usuario_form)
    @np_usuario.marshal_with(usuario_serializer, code=201)
    def post(self):
        data = usuario_form.parse_args()
        user = Usuario()
        user.insert_cadastro(**data)
        user.add()
        user.save()
        return user, 201

    def get(self, id=None):
        ...

    def patch(self, id):
        ...

    def delete(self, id):
        ...


np_usuario.add_resource(UsuarioResource, '',
                        endpoint='usuario',
                        methods=['POST', 'GET'])
np_usuario.add_resource(UsuarioResource, '/<uuid:id>',
                        endpoint='usuario-id',
                        methods=['GET', 'PATCH', 'DELETE'])
