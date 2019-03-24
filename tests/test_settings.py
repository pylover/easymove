from grbl import Connection, connection


def test_settings():
    with Connection('/dev/ttyUSB0'):
        settings = connection.settings
        assert hasattr(settings, 'step_pulse_us')

