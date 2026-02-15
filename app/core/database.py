import os
from sqlalchemy import create_engine #Фабрика для подключения к БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase #Фабрика для создания сессий
from dotenv import load_dotenv #Загружает переменные из .env


DATABASE_URL = os.getenv("DATABASE_URL",
                         "postgresql://")
class Base(DeclarativeBase) : pass

engine = create_engine(DATABASE_URL,
                       pool_size=10,
                       max_overflow=5,
                       pool_pre_ping=True,
                       echo = False)
