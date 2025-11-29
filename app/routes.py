from flask import Blueprint, jsonify, request
from app import db
from app.models import Persona

bp = Blueprint('routes', __name__)

# Obtener todas las personas
@bp.route('/api/personas', methods=['GET'])
def get_personas():
    personas = Persona.query.all()
    return jsonify([persona.to_dict() for persona in personas]), 200


@bp.route('/api/personas/<int:id>', methods=['GET'])
def get_persona(id):
    persona = Persona.query.get_or_404(id)
    return jsonify(persona.to_dict()), 200

# Crear una nueva persona
@bp.route('/api/personas', methods=['POST'])
def create_persona():
    data = request.get_json()
    
    # Validación básica
    if not all(k in data for k in ('tipo_documento', 'documento', 'nombres', 'apellidos')):
        return jsonify({
            'success': False,
            'message': 'Faltan campos obligatorios',
            'data': None
        }), 400
    
    nueva_persona = Persona(
        tipo_documento=data['tipo_documento'],
        documento=data['documento'],
        nombres=data['nombres'],
        apellidos=data['apellidos'],
        hobbie=data.get('hobbie', '')
    )
    
    try:
        db.session.add(nueva_persona)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Persona creada exitosamente',
            'data':nueva_persona.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error al crear persona: {str(e)}',
            'data': None
        }), 400

# Actualizar una persona
@bp.route('/api/personas/<int:id>', methods=['PUT'])
def update_persona(id):
    persona = Persona.query.get_or_404(id)
    data = request.get_json()
    
    persona.tipo_documento = data.get('tipo_documento', persona.tipo_documento)
    persona.documento = data.get('documento', persona.documento)
    persona.nombres = data.get('nombres', persona.nombres)
    persona.apellidos = data.get('apellidos', persona.apellidos)
    persona.hobbie = data.get('hobbie', persona.hobbie)
    
    try:
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Persona actualizada exitosamente',
            'data': persona.to_dict()
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error al actualizar persona: {str(e)}',
            'data': None
        }), 400

# Eliminar una persona
@bp.route('/api/personas/<int:id>', methods=['DELETE'])
def delete_persona(id):
    persona = Persona.query.get_or_404(id)
    
    try:
        db.session.delete(persona)
        db.session.commit()
        return jsonify({
            'success': True,
            'message': 'Persona eliminada exitosamente',
            'data': None
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error al eliminar persona: {str(e)}',
            'data': None
        }), 400