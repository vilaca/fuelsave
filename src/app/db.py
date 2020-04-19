from app.settings import settings
from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

engine = create_engine(settings.DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50)),
    Column("password", String(50)),
)

database = Database(settings.DATABASE_URL)
