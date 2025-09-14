from extensions import db, ma
from datetime import datetime
import json

class Orcamento(db.Model):
    __tablename__ = 'orcamentos'
    
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.id'), nullable=False)
    project_name = db.Column(db.String(200), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    
    # Custos breakdown
    design_hours = db.Column(db.Integer, default=0)
    frontend_hours = db.Column(db.Integer, default=0)
    backend_hours = db.Column(db.Integer, default=0)
    testing_hours = db.Column(db.Integer, default=0)
    pm_hours = db.Column(db.Integer, default=0)
    
    # Valores
    hourly_rate = db.Column(db.Float, nullable=False)
    total_hours = db.Column(db.Integer, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    
    # Metadados
    complexity_level = db.Column(db.String(20))  # baixa, media, alta
    timeline_weeks = db.Column(db.Integer)
    region = db.Column(db.String(50))  # SP, interior, remoto
    
    # JSON fields
    features = db.Column(db.Text)  # Lista de features incluídas
    assumptions = db.Column(db.Text)  # Premissas do orçamento
    risks = db.Column(db.Text)  # Riscos identificados
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def set_features(self, features_list):
        self.features = json.dumps(features_list)
    
    def get_features(self):
        return json.loads(self.features) if self.features else []
    
    def set_assumptions(self, assumptions_list):
        self.assumptions = json.dumps(assumptions_list)
    
    def get_assumptions(self):
        return json.loads(self.assumptions) if self.assumptions else []
    
    def set_risks(self, risks_list):
        self.risks = json.dumps(risks_list)
    
    def get_risks(self):
        return json.loads(self.risks) if self.risks else []
    
    def calculate_breakdown(self):
        return {
            'design': self.design_hours * self.hourly_rate,
            'frontend': self.frontend_hours * self.hourly_rate,
            'backend': self.backend_hours * self.hourly_rate,
            'testing': self.testing_hours * self.hourly_rate,
            'pm': self.pm_hours * self.hourly_rate
        }
    
    def __repr__(self):
        return f'<Orcamento {self.project_name}>'

class OrcamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orcamento
        load_instance = True
        include_fk = True

orcamento_schema = OrcamentoSchema()
orcamentos_schema = OrcamentoSchema(many=True)