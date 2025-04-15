import os
import databases
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

# DATABASE_URL = os.getenv("")
DATABASE_URL="postgresql://docker:docker@localhost:15432/postgres"
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.create_all(engine)
