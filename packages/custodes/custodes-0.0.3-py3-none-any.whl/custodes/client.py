# --------------------------------------------
import asyncio
import time
from typing import Any, Dict

import aiohttp
import codefast as cf
from codefast.asyncio.rabbitmq import publish
from rich import print

from .auth import auth
from .config import QUEUE


# —--------------------------------------------
async def _parse_ip(js: Dict) -> str:
    masked_ip = '.'.join(js['ip'].split('.')[-2:])
    return f"{js['country']} {js['region']} {js['city']} *.*.{masked_ip}"


async def ipinfo() -> str:
    fp = '/tmp/ipinfo.json'
    if cf.io.exists(fp):
        js = cf.js(fp)
        return await _parse_ip(js)
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://ipinfo.io/json?token={auth.ipinfo_token}'
            ) as resp:
                js = await resp.json()
                cf.js.write(js, fp)
                return await _parse_ip(js)


async def _post_status(service_name: str, status: Dict[str,
                                                       Any]) -> Dict[str, Any]:
    assert isinstance(status, dict)
    assert 'code' in status
    assert 'message' in status

    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    js = {
        'service_name': service_name,
        'status': status,
        'datetime': datetime,
        'ipinfo': await ipinfo()
    }
    return await publish(auth.amqp_url, QUEUE, str(js))


async def post(service_name: str,
               status: Dict[str, Any],
               loop: bool = False,
               sleep_period=60) -> None:
    while True:
        try:
            js = await _post_status(service_name, status)
            cf.info(js)
            if not loop:
                return js
        except Exception as e:
            import traceback
            cf.error({
                'error': 'post status failed',
                'exception': str(e),
                'traceback': traceback.format_exc(),
            })

        await asyncio.sleep(sleep_period)


if __name__ == '__main__':

    async def main():
        print(await post('test', {'code': 0, 'message': 'test'}, True, 0.1))

    asyncio.run(main())
