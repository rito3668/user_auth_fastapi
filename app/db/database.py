from sqlmodel import SQLModel,create_engine,Session

DATABSAE_URL = "sqlite:///./app.db"

engine = create_engine(
    DATABSAE_URL,
    echo=True
)

def get_session():
    with Session(engine) as session:
        yield session