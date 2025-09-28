#Error dan Exceptions


class ValueTooHighError(Exception):
        pass

class ValueTooLowError(Exception):
        def __init__(self, message, value):
            self.message = message
            self.value = value

def test_value(x):
        if x > 100:
            raise ValueTooHighError('value is too high')
        if x < 2:
            raise ValueTooLowError('value is too low', x)
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)