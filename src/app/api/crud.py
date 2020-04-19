from app.db import users, database, vehicles


async def get_user(username: str, password: str):
    query = users.select().where(
        username == users.c.username and password == users.c.password
    )
    return await database.fetch_one(query=query)


async def get_vehicles(username: str):
    query = (
        vehicles.select()
        .where(username == vehicles.c.owner)
        .order_by(vehicles.c.distance)
    )
    return await database.fetch_all(query=query)
