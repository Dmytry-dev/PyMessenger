#Dmytry-dev
#PyChat
#User interface
#17.08.25


import asyncpg
import asyncio
from db.connection import get_connection

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


async def sing_in(user, host, database, password):

    try:
        connect = await get_connection(user, host, database, password)

        username_input = input("Enter username\n")
        password_input = input("Enter password\n")
        
        row = await connect.fetchrow("SELECT * FROM users WHERE username = $1", username_input)
        if row["password"] == password_input:
            print(f"Login complete, welcome {row['username']}!")
        else:
            print("Wrong username or password\n")

    except Exception as ex:
        print("Mistake: ", ex)
    finally:
        if connect:
            await connect.close()
            if(DEBUG == True):
                print("Connection close\n")


async def dev_admin_panel(user, host, database, password):
    try:
        print("ADMIN MODE ACTIVATED")
        connect = await get_connection(user, host, database, password)
        print("\n--- Admin Panel ---\n1. Show all users\n2. Update user password\n3. Delete user\n4. Exit\n")
        while 1:
            admin_choice = input("Enter option:\n")

            if admin_choice == '1':
                rows = await connect.fetch("SELECT * FROM users")
                print("| ID | Username | Password | Created at |\n","-"*40)
                for row in rows:
                    created_at = row["created_at"].strftime("%Y.%m.%d %H:%M:%S") if row["created_at"] else "NULL"   
                    print(f"{row['id']:<3} | {row['username']:<10} | {row['password']:<10} | {created_at}")
                print("-"*40)

            elif admin_choice == '2':
                user_id = int(input("Enter user ID\n"))
                new_password = input("Enter new password\n")

                await connect.execute(
                    "UPDATE users SET password = $1 WHERE id = $2",
                    new_password, user_id
                )

            elif admin_choice == '3':
                user_id = int(input("Enter user ID\n"))
                await connect.execute(
                    "DELETE FROM users WHERE id =$1",
                    user_id
                )
            elif admin_choice == '4':
                break
            else:
                print("Wrong input\n")



    except Exception as ex:
        print("Mistake: ", ex)
    finally:
        if connect:
            await connect.close()
        print("Exit the admin mode\n")
        return 0