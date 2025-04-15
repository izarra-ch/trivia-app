from sqlalchemy import Table, Column, Integer, String, ARRAY
from db import metadata

# SQLAlchemy Table
questions_table = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("question", String, nullable=False),
    Column("options", ARRAY(String), nullable=False),
    Column("correct_option", String, nullable=False),
)
