from microdot.microdot_asyncio import Microdot, Request, send_file
from be_helpers.generic_helper import GenericHelper
import animation
import _thread
from ribbon import Ribbon
ribbon = Ribbon()

app = Microdot()
logger = GenericHelper.create_logger(logger_name='swagger')
GenericHelper.set_level(logger, 'debug')

@app.route('/')
async def landing_page(req: Request) -> None:
    return send_file(filename='./swagger.html',
                         status_code=200,
                         content_type='text/html')

@app.route('/api/start_animation/<path:path>')
async def start_animation(request, path):
    return ribbon.start_animation(getattr(animation, path))

@app.route('/api/display/<path:path>')
async def display(request, path):
    return ribbon.display(getattr(animation, path))

@app.route('/api/stop_animation')
async def stop_animation(request):
    return ribbon.stop_animation()

@app.route('/api/set/speed/')
async def set_speed(request):
    ribbon.speed = int(request.args['value'])

@app.route('/api/set/fps/')
async def set_fps(request):
    ribbon.fps = int(request.args['value'])


@app.route('/api/reset')
async def reset(request):
    return ribbon.reset()


def run_in_thread(host: str = '0.0.0.0',
        port: int = 80,
        debug: bool = False) -> None:
    _thread.start_new_thread(lambda: app.run(host=host, port=port, debug=debug), ())

