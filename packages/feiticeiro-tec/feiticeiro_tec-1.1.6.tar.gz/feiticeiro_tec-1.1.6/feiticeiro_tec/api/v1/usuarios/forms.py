from flask_restx.reqparse import RequestParser
from server.api.utils.forms import email_validate, password_validate

usuario_form = RequestParser()
usuario_form.add_argument('email', type=email_validate, required=True)
usuario_form.add_argument('senha', type=password_validate, required=True)
