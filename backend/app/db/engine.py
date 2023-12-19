from sqlmodel import create_engine,Session


BASE_URL_SQL = 'sqlite:///database.db'

engine  = create_engine(BASE_URL_SQL)


def get_session():
    with Session(engine) as session:
        yield session