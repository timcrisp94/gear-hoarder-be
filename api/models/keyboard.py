from datetime import datetime
from api.models.db import db


class Keyboard(db.Model):
    __tablename__ = 'keyboards'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    finish = db.Column(db.String(100))
    year = db.Column(db.String(4))
    description = db.Column(db.String(250))
    condition = db.Column(db.String(100))
    is_modified = db.Column(db.Boolean, default=False, nullable=False)
    mod_description = db.Column(db.String(250))
    is_working = db.Column(db.Boolean, default=True, nullable=False)
    on_loan = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))
    
    def __repr__(self):
      return f"Keyboard('{self.id}', '{self.make}', '{self.model}', '{self.type}'"
      
    def serialize(self):
      keyboard = {g.name: getattr(self, g.name) for g in self.__table__.columns}
      return keyboard