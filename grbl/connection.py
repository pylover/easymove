import serial

from .proxy import ObjectProxy


class Connection:
    current_connection = None
    _settings = None
    _serial = None

    def __init__(self, filename, baudrate=115200, **kw):
        self.filename = filename
        self.baudrate = baudrate
        self.kw = kw

    @property
    def settings(self):
        if self._settings is None:
            from .configuration import Settings

            self._settings = Settings(self)

            return self._settings

    def __enter__(self):
        self._serial = serial.Serial(self.filename, self.baudrate, **self.kw)
        self.__class__.current_connection = self

    def __exit__(self, exc_type, exc_value, traceback):
        self._serial.close()
        self.__class__.current_connection = None

    def send(self, data):
        self._serial.write(data.encode())

    def readlines(self):
        data = self._serial.read(10)


connection = ObjectProxy(lambda: Connection.current_connection)

