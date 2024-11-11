# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import wifi_manager.boot
from wifi_manager import WiFiManager
import _thread

wm = WiFiManager()
wm.connection_timeout = 15
wm.app.SEND_BUFSZ = 1024
result = wm.load_and_connect()
print('Connection result: {}'.format(result))

if result is False:
    print('Starting config server')
    _thread.stack_size(6*1024) 
    _thread.start_new_thread(lambda: wm.start_config(), ())
else:
    print('Successfully connected to a network :)')

print('Finished booting steps of MicroPython WiFiManager')


import webrepl
webrepl.start()

import swagger
swagger.run_in_thread()
