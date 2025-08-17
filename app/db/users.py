"""
Dmytry-dev
PyChat
User interface
17.08.25
"""

import asyncpg
import asyncio
from db.connection import get_connection, user, host, database, password

DEBUG = True

async def registration():
    connect = await get_connection(user, host, database, password)
    username_input = input("Enter username\n")
    password_input = input("Enter password\n")
    try:
        await connect.execute(
            "INSERT INTO users (username, password) VALUES($1, $2)",
            username_input,
            password_input
        )
        print("Registration complete!\n")

        if DEBUG:
            last_user = await connect.fetchrow("SELECT * FROM users ORDER BY id DESC LIMIT 1;")
            print("Last inserted user:", dict(last_user))

    except Exception as ex:
        print("Mistake:", ex)

    finally:
        if connect:
            await connect.close()
            if DEBUG:
                print("Connection Closed")