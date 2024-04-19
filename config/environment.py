# this is URI we use to talk to the database.

import os

db_URI = os.getenv("DATABASE_URL", "postgresql://localhost:5432/football_db")
SECRET = os.getenv("SECRET", "correcthorsebatterystaple")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
