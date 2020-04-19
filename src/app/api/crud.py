from app.db import users, database


async def get_user(username: str, password: str):
    query = users.select().where(
        username == users.c.username and password == users.c.password
    )
    return await database.fetch_one(query=query)
