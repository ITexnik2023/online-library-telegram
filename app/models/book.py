from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON, Float, Boolean, Text
from datetime import datetime
from ..core.database import Base

class Book(Base):

    #Основные параметры
    __tablename__ = "book_table"
    id = Column(Integer, primary_key=True, index=True) # id книги
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False) # Владелец книги

    # Метаданные книги
    name_book = Column(String, nullable=False) # Название книги
    author = Column(String(255)) # Автор
    description = Column(Text) # Краткое описание\Аннотация
    language = Column(String(10), default="ru") # Язык книги


