from django.shortcuts import render
from websocket.connection import WebSocket

def visual_feed(request):
    return render(request, 'visual_feed.html')


async def visual_feed_api(socket: WebSocket):
    await socket.accept()

    while True:
        message = await socket.receive_text()
        print(message)
