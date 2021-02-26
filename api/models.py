import json

from datetime import datetime
from extensions import db


class Goals(db.Model):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)

    pending_goals = db.Column(db.Text)
    achieved_goals = db.Column(db.Text)

    user_id = db.Column(db.String(), db.ForeignKey("user.email"))

    def data(self):
        p_goals = self.pending_goals
        a_goals = self.achieved_goals

        json_p = json.dumps(p_goals)
        json_a = json.dumps(a_goals)

        return {
            "id": self.id,
            "pending_goals": json_p,
            "achieved_goals": json_a,
            "user_id": self.user_id
        }

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
