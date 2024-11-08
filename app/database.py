from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = "aws-0-eu-central-1.pooler.supabase.com"
db = "postgres"
user = "postgres.ivahrwbpyfimyjuxniyp"
port = 6543
password = "_Phtmer%40010"
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"
# DATABASE_URL = "mysql+pymysql://root:_Phtmer%26001@127.0.0.1:3306/test_db"

# Create engine and session
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
