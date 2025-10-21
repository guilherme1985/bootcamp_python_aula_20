from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

## MOVER PARA UM ARQUIVO .env
POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydb"

# CRIA A CONEXAO E ENTAO UMA SESSAO
engine = create_engine(POSTGRES_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
