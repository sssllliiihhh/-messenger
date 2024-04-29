from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from table import table

engine = create_engine('sqlite:///db/main.db', echo=False)
Base = declarative_base()

Base = table.Base


Base.metadata.create_all(engine)

Session = sessionmaker(
    engine,
    expire_on_commit=False,
)
session = Session()
