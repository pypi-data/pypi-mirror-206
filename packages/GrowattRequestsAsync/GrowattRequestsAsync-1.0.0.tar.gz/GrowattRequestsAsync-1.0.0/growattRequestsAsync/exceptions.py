

class LoginFailedException(Exception):
    def __init__(self, msg="Login failed"):
        """
        :param msg: str
        """
        self.msg = msg
        super().__init__(self.msg)


class FetchFailedException(Exception):
    def __init__(self, msg="Failed to fetch data. Invalid parameters might be the cause."):
        """
        :param msg: str
        """
        self.msg = msg
        super().__init__(self.msg)


class InvalidTimespanException(Exception):
    def __init__(self, msg="Invalid timespan value"):
        """
        :param msg: str
        """
        self.msg = msg
        super().__init__(self.msg)