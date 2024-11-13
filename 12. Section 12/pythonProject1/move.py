class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        if self._value in (range(1, 10)) and isinstance(self._value, int):
            return True
        else:
            return False

    def get_row(self):
        if 1 <= self._value <= 3:
            return 0
        elif 4 <= self._value <= 6:
            return 1
        else:
            return 2

    def get_column(self):
        if self._value in [1, 4, 7]:
            return 0
        elif self._value in [2, 5, 8]:
            return 1
        else:
            return 2







