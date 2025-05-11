import asyncio

from collections.abc import Awaitable


async def incrementer(input: Awaitable[int]) -> int:
    return await input + 1


async def number_producer(n: int) -> int:
    return n


async def printer(input: Awaitable[int]):
    print(await input)


async def main():
    async with asyncio.TaskGroup() as tg:
        one = tg.create_task(number_producer(1))
        _ = tg.create_task(printer(one))
        increment_one = tg.create_task(incrementer(one))
    print(one.result())
    print(increment_one.result())


if __name__ == "__main__":
    asyncio.run(main())
