from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

STR_CONNECTION = 'mysql://root:root@localhost/test'
engine = create_engine(STR_CONNECTION, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models.models_usuario
    import models.models_colaborador
    import models.models_cliente
    Base.metadata.create_all(bind=engine)