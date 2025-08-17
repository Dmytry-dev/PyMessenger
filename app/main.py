"""
Dmytry-dev
PyChat
Main 
16.08.2025
"""
import asyncio
import asyncpg
from db.connection import get_connection
from db.users import registration




def main():
    user_choice = input("Sing in - 1\nRegistration - 2\nExit - 3\n")
    if user_choice == "1":
        pass
    elif user_choice == "2":
        asyncio.run(registration())
    elif user_choice == "3":
        return
    else:
        print("Wrong choice\n")

main()