from server.database import db
from .base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from loguru import logger


class Usuario(Base, db.Model):
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def insert_cadastro(self, email, senha):
        logger.debug('Inserindo cadastro do usuário')
        self.email = email
        self.senha = generate_password_hash(senha)

    def login(self, senha):
        logger.debug('Verificando senha')
        return check_password_hash(self.senha, senha)
