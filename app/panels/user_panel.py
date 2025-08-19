#Dmytry-dev
#Pychat
#User panel
#18.08.25

import asyncio
import asyncpg
from db.connection import get_connection

async def user_panel(current_id, user, host, database, password):

    pool = await asyncpg.create_pool(
        user = user,
        host = host,
        database = database,
        password = password,
        port = 5432,
        min_size = 1,
        max_size = 5
    )

    async with pool.acquire() as connection:
        while 1:
            rows = await connection.fetch("""
                SELECT users.id, users.username
                FROM friends
                JOIN users ON friends.friends_id = users.id
                WHERE friends.user_id = $1
                """, current_id)

            print("Your contacts:")
            i = 0
            for row in rows:
                    i += 1
                    print(f"{i}. {row['id']}-{row['username']}")
            print("Add contact - +\nExit - e\n")
            user_choice = input("")
            if(user_choice == '+'):
                contact_id = input("Enter contact id\n")
                row = await connection.fetchrow("SELECT id FROM users WHERE id = $1", int(contact_id))
                if(row):
                    await connection.execute("""INSERT INTO friends (user_id, friends_id) VALUES($1, $2)
                                                ON CONFLICT DO NOTHING""",
                                                current_id, int(contact_id)
                                            )
                else:
                    print("This user dont exist")
            if(user_choice == 'e'):
                return
