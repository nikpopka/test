import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI



app = FastAPI()

engine = create_async_engine('sqlite+aiosqlite:///books.db')


new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    autor: Mapped[str]



@app.get("/test")
def test():
    return 11

@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(Base.metadata.drop_all)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8001)