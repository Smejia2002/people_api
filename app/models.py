from app import db
from datetime import datetime, timezone

class Persona(db.Model):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    tipo_documento = db.Column(db.String(50), nullable=False)
    documento = db.Column(db.String(50), unique=True, nullable=False)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    hobbie = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'tipo_documento': self.tipo_documento,
            'documento': self.documento,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'hobbie': self.hobbie,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f"<Persona {self.nombres} {self.apellidos}>"