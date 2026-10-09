
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import make_url

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing")

if os.name == "nt":
    CA_PATH = os.path.join(os.path.dirname(__file__), "ca.pem")
else:
    CA_PATH = "/etc/ssl/certs/ca-certificates.crt"

parsed_url = make_url(DATABASE_URL)

# Print diagnostic information only — never print the password.
print("DB driver:", parsed_url.drivername)
print("DB username:", parsed_url.username)
print("DB host:", parsed_url.host)
print("DB database:", parsed_url.database)

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

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()