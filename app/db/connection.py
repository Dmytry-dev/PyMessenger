#Dmytry-dev
#PyChat
#Connection to Database
#15.08.25


import asyncpg
import asyncio
import os
from dotenv import load_dotenv

DEBUG = True


    
async def get_connection(user, host, database, password):

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
            return connection                        

    