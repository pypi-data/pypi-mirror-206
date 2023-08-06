from flask_restx import ValidationError
from validate_docbr import CPF, CNPJ
import re


def number_required(value):
    if not re.search(r'[0-9]', value):
        raise ValidationError('Conter um numero é obrigatório')
    return value


def lower_case_required(value):
    if not re.search(r'[a-z]', value):
        raise ValidationError('Conter uma letra minuscula é obrigatório')
    return value


def upper_case_required(value):
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Conter uma letra maiuscula é obrigatório')
    return value


def special_character_required(value):
    if not re.search(r'[!@#$%&*()_+=-]', value):
        raise ValidationError('Conter um caracter especial é obrigatório')
    return value


def length_required(value):
    if len(value) < 8:
        raise ValidationError('Conter no minimo 8 caracteres é obrigatório')
    return value


def strip_required(value):
    if value.strip() == '':
        raise ValidationError('O campo não pode ser vazio')
    return value.strip()


def password_validate(value):
    number_required(value)
    lower_case_required(value)
    upper_case_required(value)
    special_character_required(value)
    length_required(value)
    return value


def cpf_validate(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError('CPF inválido')
    return value


def cnpj_validate(value):
    cnpj = CNPJ()
    if not cnpj.validate(value):
        raise ValidationError('CNPJ inválido')
    return value


def cnpj_cpf_validate(value):
    try:
        cpf_validate(value)
    except ValidationError:
        try:
            cnpj_validate(value)
        except ValidationError:
            raise ValidationError('CPF/CNPJ inválido')
    return value


def email_validate(value):
    if not re.match(r'^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?', value):
        raise ValidationError('Email inválido')
    return value


def phone_validate(value):
    value = re.sub(r'\D', '', value.group())
    if len(value) not in (10, 11):
        raise ValidationError('Telefone inválido')
    return value


def cep_validate(value):
    value = re.search(r'[0-9]{5}(-)?[0-9]{3}', value)
    if not value:
        raise ValidationError('CEP inválido')
    return value


def unique_fields_validate(field, query, field_name):
    def inner(value):
        if query.filter(field == value).first():
            raise ValidationError(f'{field_name} já cadastrado')
        return value
    return inner


def password_validate(value):
    number_required(value)
    lower_case_required(value)
    upper_case_required(value)
    special_character_required(value)
    length_required(value)
    return value


def boolean_validate(value):
    error = ValidationError(
        'Valor deve ser [True,False,"true", "false", 1, 0,"1", "0"]')
    if isinstance(value, bool):
        return value

    elif isinstance(value, str):
        value = value.lower()
        if value not in ('true', 'false', '1', '0'):
            raise error
        return True if value == 'true' or value == '1' else False

    elif isinstance(value, int):
        if value not in (1, 0):
            raise error
        return True if value == 1 else False

    raise error
