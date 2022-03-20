import aiohttp
import json


async def get(url, headers=None):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            result = await response.read()
            if response.status in (200, 207):
                return {
                    'satus': True,
                    'status_code': response.status,
                    'data': json.loads(result)
                }
            return {
                'status_code': response.status
            }
