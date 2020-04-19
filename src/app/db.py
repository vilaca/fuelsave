from app.settings import settings
from app.api import hashing_service
from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
import csv
import os

engine = create_engine(settings.DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), index=True),
    Column("password", String(50)),
)

vehicles = Table(
    "vehicles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("distance", Integer),
    Column("owner", String(50), index=True),
)


async def migrate():
    if await database.fetch_one(query=users.select()):
        return
    with open(os.path.join(settings.DATA_IMPORT_PATH, "users.csv")) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            query = users.insert().values(
                username=row[0], password=hashing_service.hash(row[1])
            )
            await database.execute(query=query)
    with open(os.path.join(settings.DATA_IMPORT_PATH, "vehicles.csv")) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            query = vehicles.insert().values(
                id=int(row[0]), distance=int(row[1]), owner=row[2]
            )
            await database.execute(query=query)


database = Database(settings.DATABASE_URL)
