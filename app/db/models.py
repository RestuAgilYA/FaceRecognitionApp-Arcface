from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Face(Base):
    __tablename__ = "faces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    embedding = Column(LargeBinary, nullable=False)
    image_path = Column(String, nullable=True)  # New