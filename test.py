import asyncio
import search


async def main():
    while True:
        print(await search.organic_search(input(">> ")))


asyncio.run(main())
