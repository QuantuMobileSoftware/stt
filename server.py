import os
import sys
from datetime import datetime
from aiohttp import web
import logging
from model_wrapper import ModelWrapper


if sys.flags.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


routes = web.RouteTableDef()
try:
    model_wrapper = ModelWrapper()
except Exception as e:
    log.exception("Error during load of ModelWrapper")


@routes.post("/api/stt")
async def process_stt(request):
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}.wav"
    with open(filename, 'wb') as fd:
        while True:
            chunk = await request.content.read()
            if not chunk:
                break
            fd.write(chunk)

    if os.stat(filename).st_size != 0:
        text = await model_wrapper.predict_async(filename)
        data = {"Text": text}
        return web.json_response(data)
    else:
        os.remove(filename)
        return web.json_response({})


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, port=9000)
