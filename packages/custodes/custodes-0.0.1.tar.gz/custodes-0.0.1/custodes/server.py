# --------------------------------------------
import asyncio
import datetime
import os
from typing import Any, Dict

import codefast as cf
from codefast.asyncio.rabbitmq import consume
from rich import print

from .auth import auth
from .config import QUEUE


# —--------------------------------------------
async def get_db():
    return cf.osdb(os.path.join('/tmp/', QUEUE))


async def _sync_status(message: bytes) -> Dict[str, Any]:
    message_str = message.decode()
    js = cf.js(message_str)
    service_name = js['service_name']
    db = await get_db()
    await db.set(service_name, js)


async def generate_summary() -> Dict[str, Any]:

    def parse_value(v) -> str:
        js = cf.js(v)
        dtime = js['datetime']
        last_active = datetime.datetime.strptime(dtime, "%Y-%m-%d %H:%M:%S")
        time_diff = datetime.datetime.now() - last_active

        def is_okay(time_diff, code: int) -> bool:
            return time_diff > datetime.timedelta(minutes=10) and code == 0

        if is_okay(time_diff, js['status']['code']):
            return {
                'service_name': js['service_name'],
                'status': 'ok',
                'last_active': dtime,
                'ipinfo': js['ipinfo'],
            }
        else:
            return {
                'service_name': js['service_name'],
                'status': 'error',
                'last_active': dtime,
                'ipinfo': js['ipinfo'],
                'message': js['status']['message']
            }

    db = await get_db()
    return [parse_value(v) for v in db.values()]


async def get():
    return await asyncio.gather(consume(auth.amqp_url, QUEUE, _sync_status),
                                generate_summary())


if __name__ == '__main__':
    asyncio.run(get())
