from db import engine

try:
    with engine.connect() as connection:
        print("TiDB Cloud connected successfully!")
except Exception as e:
    print("Connection failed:", e)