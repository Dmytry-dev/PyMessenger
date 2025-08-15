'''
Dmytry-dev
PyChat
Connection to Database
15.08.25
'''

import asyncpg
import asyncio
import os
from dotenv import load_dotenv

DEBUG = True

load_dotenv()

user = os.getenv("user")
host = os.getenv("host")
database = os.getenv("database")
password = os.getenv("password")

if(DEBUG == True):
    print(user, host, database, password)
    
async def connection(user, host, database, password):

    try:
        connection = await asyncpg.connect(
            user = user,
            host = host,
            database = database,
            password = password
        )

        if(DEBUG == True):
            result = await connection.fetchval("SELECT 1;")
            print("DB test", result)

    except Exception as ex:
        print("Mistake: ", ex)
    finally:
        if connection:
            await connection.close()
            
            if(DEBUG == True):
                print("Connection closed")
            

asyncio.run(connection(user, host, database, password))
    