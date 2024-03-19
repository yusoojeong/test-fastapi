from sqlalchemy import Column,  String

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "test_user"

    id = Column(
        String(length=128),
        primary_key=True,
        unique=True,
    )
    password = Column(
        String(length=128),
        nullable=False,
    )
