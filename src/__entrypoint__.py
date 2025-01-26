import asyncio
from random import randint

async def processor(name):
    while True:
        print(f"Изображаем бурную деятельность № {name}")
        await asyncio.sleep(randint(0, 15))
        

async def runner():
    await asyncio.gather(*[
       asyncio.create_task(processor(num)) for num in range(1, 6)
    ])


def main():
    print("Начинаем работу")
    try:
        asyncio.run(runner())
    except KeyboardInterrupt:
        print("Заканчиваем работу")
