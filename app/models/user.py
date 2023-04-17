from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.session import Base


class UserModel(Base):
    """Classe de modelo para usuário"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(400), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"
