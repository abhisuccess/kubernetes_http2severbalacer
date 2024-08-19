import asyncio
from aiohttp import web
import logging

# Configure logging
logging.basicConfig(filename='/home/abhi1/server1.log',  # Path to your log file
                    level=logging.INFO,  # Log level
                    format='%(asctime)s - %(levelname)s - %(message)s')  # Log format

async def handle(request):
    logging.info('Received request at %s', request.path)  # Log each request
    await asyncio.sleep(1)  # Simulate some processing time
    return web.Response(text="Hello from Server 1")

app = web.Application()
app.router.add_get('/hello', handle)

web.run_app(app, port=8081)

