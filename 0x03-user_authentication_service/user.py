#!/usr/bin/env python3
""" SQLAlchemy model for User
"""

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

