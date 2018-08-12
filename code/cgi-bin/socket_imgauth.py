#!/usr/bin/python36
import asyncio
import websockets
import base64
import face
import cookie
from http import cookies


async def img_auth(websocket, path):
    # Waiting for client to send image URI
    name = await websocket.recv()

    # Image URI is base64 encoded and contains some extra characters
    name = (name.split(','))[-1]
    imgdata = base64.b64decode(name)
    #print(imgdata)

    # Write image received during login to disk
    filename = './images/tmp/unknown_face.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    try:
        # face.py contains a method 'whoiam' to match the client's received image with
        # already registered image of client.
        match_face = face.whoiam(filename)

        if match_face == True:
            print('Matched')
            # Create a cookie object
            ck = cookies.SimpleCookie()

            # set_cookie(username) method create and generates a cookie and
            # return its value. Check cookie.py for more info.
            ck = cookie.set_cookie('kb')

            # Get cookie 'ck' value and assign it to variable 'data'
            data = ck['secret'].value

            # Send 'data' variable value to the client browser
            await websocket.send(data)
    except:
        print('Not matched')
        # Send failed message to client browser
        await websocket.send('failed')

# Start server websockets on port no. 8765 and allow access to everyone(0.0.0.0)
start_server = websockets.serve(img_auth, '0.0.0.0', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
