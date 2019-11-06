from flask import Blueprint, jsonify, request
from services.professores_service import \
    listar as service_listar, \
    localizar as service_localiza, \
    criar as service_criar, \
    remover as service_remover, \
    atualizar as service_atualiza, \
    reseta as service_reseta

professores_app = Blueprint('professores_app', __name__, template_folder='templates')


@professores_app.route('/professores', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(lista)


@professores_app.route('/professores/<int:id>', methods=['GET'])
def localizar(id):
    p = service_localiza(id)
    if p != None:
        return jsonify(p)
    return jsonify({'erro': 'professor sem nome'}), 400


@professores_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()
    if novo_professor == None:
        return jsonify({'erro': 'dados não informados'}), 400
    if 'id' not in novo_professor:
        return jsonify({'erro': 'id não informado'}), 400
    p = service_criar(novo_professor)
    if p == None:
        return jsonify({'erro': 'professor Já cadastrado'}), 400
    return jsonify(p)


@professores_app.route('/professores/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido == 1:
        return jsonify({'sucesso': 'professor removido com sucesso'}), 202
    return jsonify({'erro': 'professor nao encontrado'}), 400


@professores_app.route('/professores/<int:id>', methods=['PUT'])
def atualiza(id):
    professor_data = request.get_json()
    atualizado = service_atualiza(id, professor_data['nome'])
    if atualizado is not None:
        return jsonify(atualizado)
    if atualizado is None:
        return jsonify({'erro': 'professor não encontrado'}), 400
    if ('nome' not in professor_data):
        return jsonify({'erro': 'professor sem nome'}), 400


@professores_app.route('/professores/reseta', methods=['POST'])
def reseta_professores():
    service_reseta()
    return jsonify({'sucesso': 'professores resetados'}), 202
