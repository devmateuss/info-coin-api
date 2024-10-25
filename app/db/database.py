from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import aplication_settings

Base = declarative_base()

class Config:
    session_maker: sessionmaker | None = None

def config_alchemy():
    engine = create_engine(aplication_settings.database_url)
    Config.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    create_all_tables(engine)

def create_all_tables(engine):
    """Cria todas as tabelas definidas pelo Base."""
    Base.metadata.create_all(bind=engine)

def get_session():
    """
    Retorna uma nova sessão de banco de dados.
    Deve ser usado em contexto de `with` para garantir o fechamento da sessão.
    """
    if not Config.session_maker:
        raise RuntimeError("Session maker is not configured. Call `config_alchemy` first.")
    return Config.session_maker()
