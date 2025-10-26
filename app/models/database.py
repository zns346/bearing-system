# create_tables.py
from .database import engine, Base  # core/database.py
from app.models.bearing import Bearing  # sibling models folder via full package name

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")
