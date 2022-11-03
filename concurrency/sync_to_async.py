import asyncio
from time import perf_counter

import requests

VELIB_URL = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"

async def counter(until:int=10) -> None:
    now = perf_counter()
    print("Counter started ...")
    for index in range(until):
        last = perf_counter()
        await asyncio.sleep(0.01)
        now = perf_counter()
        print(f"{index + 1 }: Was asleep for {now-last} seconds")


def send_request(url:str) -> int:
    print("Sending HTTP Request")
    response = requests.get(url)
    return response.status_code

async def send_async_request(url:str) -> int:
    return await asyncio.to_thread(send_request, url)


async def main1() -> None:
    task = asyncio.create_task(counter())
   
    # status_code = send_request(url) # synchronous request sending
    
    status_code = await send_async_request(VELIB_URL) # Asynchronous request sending
    # - In this way, we do not have to wait for the request to terminate
    # - to start counting
    print(f"Got HTTP response with status: {status_code}")
    await task

    

async def main2() -> None:

    # --- To simplify the code above, in `main1` function, since we have 2 asunchronous functions, 
    # we can run them concurrently by awaiting them at the same time,
    # in 1line by using the `gather` method
    
    status_code, _ = await asyncio.gather(send_async_request(VELIB_URL), counter())
    print(f"Got HTTP response with status: {status_code}")
    
    
    
if __name__ == "__main__":
    # asyncio.run(main1())
    asyncio.run(main2())
