#Dmytry-dev
#PyChat
#Main 
#16.08.2025

import asyncio
import asyncpg
from dotenv import load_dotenv
import os
from db.connection import get_connection
from db.users import registration, sing_in, dev_admin_panel


DEBUG = True


def main():

    load_dotenv()

    user = os.getenv("user")
    host = os.getenv("host")
    database = os.getenv("database")
    password = os.getenv("password")
    admin_password = os.getenv("admin_password")

    if(DEBUG == True):
        print(user, host, database, password)

    while 1:
        user_choice = input("Sing in - 1\nRegistration - 2\nExit - 3\n")
        if user_choice == "1":
            asyncio.run(sing_in(user, host, database, password))
        elif user_choice == "2":
            asyncio.run(registration(user, host, database, password))
        elif user_choice == "3":
            return 0
        
        #Admin panel for quick access to all data for debugging during development
        elif user_choice == admin_password:
            asyncio.run(dev_admin_panel(user, host, database, password))

        else:
            print("Wrong choice\n")

main()