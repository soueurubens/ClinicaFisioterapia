from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


url = r'postgresql://postgres:engenharia12345@db.bzmmeitjywbenhrggkgq.supabase.co:5432/postgres'
engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try: 
        yield db
    except:
        db.close()
