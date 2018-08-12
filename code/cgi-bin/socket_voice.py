#!/usr/bin/python36
import asyncio
import websockets
import nlp


async def get_command(websocket, path):
    # Waiting for client to send text command to process
    command = await websocket.recv()
    try:
        print(command)
        # Use nlp module to get custom URL depending on the query
        url = nlp.process_query(command)

        # Send URL to the client
        await websocket.send(url)
    except:
        # Send failed message to the client
        await websocket.send('failed')


start_server = websockets.serve(get_command, '0.0.0.0', 8760)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
