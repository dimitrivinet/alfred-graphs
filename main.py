import asyncio
import websockets
import json
import random
import time

connected = set()


def format_pos(xyzrpy):
    return {
        "x": xyzrpy[0],
        "y": xyzrpy[1],
        "z": xyzrpy[2],
        "roll": xyzrpy[3],
        "pitch": xyzrpy[4],
        "yaw": xyzrpy[5],
    }


async def loop(websocket):
    while True:
        msg = format_pos(
            [
                random.randint(-100, 100) / 100,
                random.randint(-100, 100) / 100,
                random.randint(-100, 100) / 100,
                random.randint(-100, 100) / 100,
                random.randint(-100, 100) / 100,
                random.randint(-100, 100) / 100,
            ]
        )
        print(msg)
        await websocket.send(json.dumps(msg))

        time.sleep(1.0 / 24)


async def connect_hook(websocket, _):
    global connected

    if websocket not in connected:
        connected.add(websocket)
        asyncio.create_task(loop(websocket))


def main():
    start_server = websockets.serve(connect_hook, "0.0.0.0", 8000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
