from .proxy import ObjectProxy


class Settings:
    _step_pulse_us = None

    def __init__(self, connection):
        self.connection = connection
        self.reload()

    def reload(self):
        self.connection.send('$$')
        for line in self.connection.readlines():
            print(line)

    def update_field(self, key, value):
        self.connection.send(f'${key}={value}')
        self.reload()

    @property
    def step_pulse_us(self):
        return self._step_pulse_us

    @step_pulse_us.setter
    def ster_pulse_us(self, value):
        self.update_field(STEP_PULSE_FIELD, value)

