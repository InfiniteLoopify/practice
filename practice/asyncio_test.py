import asyncio


async def func(param):
    await asyncio.sleep(param)
    return param


async def producer(q: asyncio.Queue, obj_id=1):
    for i in range(3):
        print(f"put ({obj_id}) <<-- {i}")
        await q.put(i)
        await asyncio.sleep(0.5)


async def consumer(q: asyncio.Queue, obj_id=1):
    while True:
        x = await q.get()
        print(f"get ({obj_id}) -->> {x}")
        q.task_done()


async def main():

    # start = time.perf_counter()
    # for i in range(4):
    #     print(await func(i))
    # print(f"Finished in {time.perf_counter() - start:.2f} seconds")

    # start = time.perf_counter()
    # print(await asyncio.gather(*(func(i) for i in range(4))))
    # print(f"Finished in {time.perf_counter() - start:.2f} seconds")

    q = asyncio.Queue(maxsize=2)
    c, p = 2, 2
    cons = [asyncio.create_task(consumer(q, i)) for i in range(c)]
    prods = [asyncio.create_task(producer(q, i)) for i in range(p)]
    await asyncio.gather(*prods)

    # for i in asyncio.as_completed(prods):
    #     print(await i)

    await q.join()

    for i in cons:
        i.cancel()

    await asyncio.sleep(2)
    for i in asyncio.all_tasks():
        print(i)


if __name__ == "__main__":
    asyncio.run(main(), debug=True)

# NOTES:
# create_task -> start background task
# gather -> wait for all tasks to finish, then return results
# as_completed -> return result as the task is finished
