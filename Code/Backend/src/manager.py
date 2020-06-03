from .backend.submanagers.rest import RestManager
from .backend.submanagers.sensors import SensorManager
from .backend.util.logger import log
import time as t

class Manager():
    def __init__(self, debug):
        self.debug = debug

    def setup(self):
        self.rest_manager = RestManager(self.debug)

        t.sleep(1.5)
        self.sensor_manager = SensorManager()

    def register(self):
        pass

    def start(self):
        self.active = True

        self.setup()

        self.sensor_manager.start()
        self.rest_manager.start()

    def stop(self, exception = False):
        log.info('MANAGER', 'Killing all threads...')

        if hasattr(self, 'sensor_manager'):
            self.sensor_manager.kill()
        if hasattr(self, 'rest_manager'):
            self.rest_manager.kill()


    def stop_signal(self, signum, frame):
        self.stop()
