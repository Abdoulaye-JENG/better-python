import asyncio
from random import randint
from time import perf_counter

from req_http import http_get_async, http_get_sync

MAX_POKEMON = 700
MAX_LOOP_NUMBER = 20


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1,MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon.get("name"))


async def get_random_pokemon_name_async() -> str:
    pokemon_id = randint(1,MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get_async(pokemon_url)
    return str(pokemon.get("name"))

async def main1():
    """
    For this first __main__ function,
    we are retrieving pokemons asuynchronously, but we still have to wait,
    for every request to finish, before attempting a new one.
    """
    # pokemon_name = get_random_pokemon_name_sync()
    start_time = perf_counter()
    for _ in range(MAX_LOOP_NUMBER):
        pokemon_name = await get_random_pokemon_name_async()
        print(f"Pokemon Name: {pokemon_name}")
    print(f"Total time in synchronous/waiting mode:  {perf_counter() - start_time} seconds")

async def main2(): # Gather
    """
    For this 2nd __main__ function,
    we are retrieving pokemons asuynchronously, but we do not have to wait,
    requests are executed in parallel. It's done using asyncio's <gather>
    method:
    """
    start_time = perf_counter()
    tasks = [get_random_pokemon_name_async() for _ in range(MAX_LOOP_NUMBER)]
    result = await asyncio.gather(*tasks)
    print(" => Pokemons: ")
    print(result)
    print(f"Total time in asynchronous mode:  {perf_counter() - start_time} seconds")
    # for _ in range(25):
    #     pokemon_name = await get_random_pokemon_name_async()
    #     print(f"Pokemon Name: {pokemon_name}")


if __name__ == "__main__":
    print("***** SYNCHRONOUS ******")
    asyncio.run(main1())
    print("***** ASYNCHRONOUS ******")
    asyncio.run(main2())
    