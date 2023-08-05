from flask_restx import Resource
from server.api import api
from server.database.models import Usuario

np_usuario = api.namespace(
    'usuario', description='Operações relacionadas a usuários')


class UsuarioResource(Resource):
    def post(self):
        user = Usuario()
        user.insert_cadastro()
        user.add()
        user.save()
        return user

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
