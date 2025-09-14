from app import db, ma
from datetime import datetime
import json

class Conversation(db.Model):
    __tablename__ = 'conversations'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), unique=True, nullable=False)
    messages = db.Column(db.Text, default='[]')  # JSON array de mensagens
    project_type = db.Column(db.String(50))
    requirements = db.Column(db.Text)  # JSON dos requisitos coletados
    status = db.Column(db.String(20), default='active')  # active, completed, abandoned
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    orcamento = db.relationship('Orcamento', backref='conversation', uselist=False)
    
    def add_message(self, role, content):
        messages = json.loads(self.messages) if self.messages else []
        messages.append({
            'role': role,
            'content': content,
            'timestamp': datetime.utcnow().isoformat()
        })
        self.messages = json.dumps(messages)
        self.updated_at = datetime.utcnow()
    
    def get_messages(self):
        return json.loads(self.messages) if self.messages else []
    
    def set_requirements(self, requirements_dict):
        self.requirements = json.dumps(requirements_dict)
    
    def get_requirements(self):
        return json.loads(self.requirements) if self.requirements else {}
    
    def __repr__(self):
        return f'<Conversation {self.session_id}>'

class ConversationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Conversation
        load_instance = True
        include_fk = True

conversation_schema = ConversationSchema()
conversations_schema = ConversationSchema(many=True)