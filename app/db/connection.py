import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine
import asyncpg
from dotenv import load_dotenv
import os

load_dotenv(".env")
create_async_engine(os.environ.get("DATABASE_URL"))