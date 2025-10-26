# backend/python/app/core/create_tables.py
from .database import engine, Base
from app.models.bearing import Bearing  # ✅ Use 'app' as top-level package

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")
