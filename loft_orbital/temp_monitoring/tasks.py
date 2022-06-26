import asyncio
import json
import os
from datetime import datetime, timezone

import django
import websockets
from asgiref.sync import sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loft_orbital.settings')
django.setup()

from loft_orbital.temp_monitoring.models import Temperature  # noqa


async def process_msg(data: dict) -> None:
    try:
        t = Temperature(timestamp=datetime.now(timezone.utc),
                        value=data['payload']['data']['temperature'])
        await sync_to_async(t.save)()
        print(f"{t} saved")
    except:
        print(f'Could not handle this temp: {data}')


async def capture_data() -> None:
    uri: str = f"ws://{os.getenv('WS_HOST','temp')}:4000/graphql"
    start: dict = {
        "type": "start",
        "payload": {"query": "subscription { temperature }"}
    }
    async with websockets.connect(uri, subprotocols=["graphql-ws"]) as websocket:
        await websocket.send(json.dumps(start))
        while True:
            data = await websocket.recv()
            asyncio.create_task(process_msg(json.loads(data)))

if __name__ == "__main__":
    print('Running')
    asyncio.run(capture_data())
