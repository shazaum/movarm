from app import db

class MovimentoManual(db.Model):
    __tablename__ = 'movimento_manual'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    moveup = db.Column(db.Integer, nullable=True)
    movedown = db.Column(db.Integer, nullable=True)
    moveright = db.Column(db.Integer, nullable=True)
    moveleft = db.Column(db.Integer, nullable=True)

    def __init__(self, moveup, movedown, moveright, moveleft):
        self.moveup = moveup
        self.movedown = movedown
        self.moveright = moveright
        self.moveleft = moveleft