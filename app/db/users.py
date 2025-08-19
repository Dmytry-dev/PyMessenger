#Dmytry-dev
#PyChat
#User interface
#17.08.25


import asyncpg
import asyncio
from db.connection import get_connection
from panels.user_panel import user_panel

DEBUG = True

async def registration(user, host, database, password):
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

        current_id = await connect.fetchval("SELECT id FROM users WHERE username = $1;", username_input)
        await connect.close()
        await user_panel(current_id, user, host, database, password)

    except Exception as ex:
        print("Problem with registration. Please try again.")
        if DEBUG == True:
            print("Mistake:", ex)
        if connect:
            await connect.close()
            if(DEBUG == True):
                print("Connection close\n")
        return

    finally:
        if connect:
            await connect.close()
            if DEBUG:
                print("Connection Closed")
            


async def sing_in(user, host, database, password):

    try:
        connect = await get_connection(user, host, database, password)

        username_input = input("Enter username\n")
        password_input = input("Enter password\n")
        
        row = await connect.fetchrow("SELECT * FROM users WHERE username = $1", username_input)
        if row["password"] == password_input:
            print(f"Login complete, welcome {row['username']}!")
            current_id = await connect.fetchval("SELECT id FROM users WHERE username = $1", username_input)
            await connect.close()
            await user_panel(current_id, user, host, database, password)
        else:
            print("Wrong username or password\n")


    except Exception as ex:
        print("Problem with login. Please tre again.")
        if DEBUG == True:
            print("Mistake:", ex)   
        if connect:
            await connect.close()
            if(DEBUG == True):
                print("Connection close\n")
        return
         
    
    finally:
        if connect:
            await connect.close()
            if(DEBUG == True):
                print("Connection close\n")
            



