import asyncio

import websockets


async def main():

    uri = (
        "ws://127.0.0.1:8000/ws/chat"
    )

    async with websockets.connect(
        uri
    ) as websocket:

        print(
            "Connected to WebSocket."
        )

        await websocket.send(
            "What is Generative AI?"
        )

        while True:

            response = (
                await websocket.recv()
            )

            print(
                response
            )

            if '"type":"answer"' in response:

                break


if __name__ == "__main__":
    asyncio.run(main())