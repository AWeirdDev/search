import asyncio

from .primp import Client
from .search import get_djs, get_page_layout_from_djs
from .utils import raise_for_status

try:
    import orjson as json
except ModuleNotFoundError:
    import json


async def organic_search(query: str) -> dict:
    client = Client(impersonate="chrome_127", verify=False)
    response = await asyncio.to_thread(
        client.get, "https://start.duckduckgo.com", params={"q": query}
    )
    raise_for_status(response)

    djs_url = get_djs(response.text)
    djs = await asyncio.to_thread(client.get, "https://links.duckduckgo.com" + djs_url)
    raise_for_status(djs)

    layout = get_page_layout_from_djs(djs.text)

    return json.loads(layout[:-4].split(".load('d',")[1] + "]")
