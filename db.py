from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL for TiDB Cloud
DATABASE_URL = (
    "mysql+pymysql://2KQiTpvVuRuMNUw.root:sEkAxEzx1hmXFEK4"
    "@gateway01.ap-northeast-1.prod.aws.tidbcloud.com:4000/test"
)

# CA certificate
CA_PATH = r"C:\Users\Administrator\Desktop\ai_career_copilot\ca.pem"

# Creating database engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": CA_PATH,
            "check_hostname": True,
        }
    },
)

# Creating sessions
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# Creating the base class for ORM
Base = declarative_base()