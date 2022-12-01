"""Module describing exceptions for inference endpoint"""


class InvalidCategoryValueError(Exception):
    """Exception raised when invalid value in request"""

    def __init__(self, value, enumerator, message=None):
        """Set message depending on value and enumerator"""
        self._value = value
        self._enumerator = enumerator
        self._set_message(message)
        super().__init__(self.message)

    def _set_message(self, message):
        if message is not None:
            self.message = message
        else:
            self.message = (
                "Received a categorical value not within trained set. "
                f"{self._value} not in {[v.value for v in self._enumerator]}."
            )
