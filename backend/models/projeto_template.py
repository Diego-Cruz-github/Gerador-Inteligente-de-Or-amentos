from app import db, ma
import json

class ProjetoTemplate(db.Model):
    __tablename__ = 'projeto_templates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # app, website, sistema
    description = db.Column(db.Text)
    
    # Horas base por categoria
    base_design_hours = db.Column(db.Integer, default=0)
    base_frontend_hours = db.Column(db.Integer, default=0)
    base_backend_hours = db.Column(db.Integer, default=0)
    base_testing_hours = db.Column(db.Integer, default=0)
    base_pm_hours = db.Column(db.Integer, default=0)
    
    # Multiplicadores por complexidade
    complexity_multipliers = db.Column(db.Text)  # JSON: {baixa: 0.8, media: 1.0, alta: 1.5}
    
    # Features típicas
    typical_features = db.Column(db.Text)  # JSON array
    optional_features = db.Column(db.Text)  # JSON array com custos adicionais
    
    # Perguntas contextuais para este tipo de projeto
    context_questions = db.Column(db.Text)  # JSON array
    
    is_active = db.Column(db.Boolean, default=True)
    
    def set_complexity_multipliers(self, multipliers_dict):
        self.complexity_multipliers = json.dumps(multipliers_dict)
    
    def get_complexity_multipliers(self):
        return json.loads(self.complexity_multipliers) if self.complexity_multipliers else {}
    
    def set_typical_features(self, features_list):
        self.typical_features = json.dumps(features_list)
    
    def get_typical_features(self):
        return json.loads(self.typical_features) if self.typical_features else []
    
    def set_optional_features(self, features_list):
        self.optional_features = json.dumps(features_list)
    
    def get_optional_features(self):
        return json.loads(self.optional_features) if self.optional_features else []
    
    def set_context_questions(self, questions_list):
        self.context_questions = json.dumps(questions_list)
    
    def get_context_questions(self):
        return json.loads(self.context_questions) if self.context_questions else []
    
    def calculate_hours(self, complexity='media', additional_features=None):
        multiplier = self.get_complexity_multipliers().get(complexity, 1.0)
        
        hours = {
            'design': int(self.base_design_hours * multiplier),
            'frontend': int(self.base_frontend_hours * multiplier),
            'backend': int(self.base_backend_hours * multiplier),
            'testing': int(self.base_testing_hours * multiplier),
            'pm': int(self.base_pm_hours * multiplier)
        }
        
        # Adicionar horas de features opcionais
        if additional_features:
            optional_features = self.get_optional_features()
            for feature in additional_features:
                for opt_feature in optional_features:
                    if opt_feature['name'] == feature:
                        for key in hours:
                            hours[key] += opt_feature.get(f'{key}_hours', 0)
        
        return hours
    
    def __repr__(self):
        return f'<ProjetoTemplate {self.name}>'

class ProjetoTemplateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProjetoTemplate
        load_instance = True

projeto_template_schema = ProjetoTemplateSchema()
projeto_templates_schema = ProjetoTemplateSchema(many=True)