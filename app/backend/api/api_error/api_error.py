class APIError(Exception):
    """ Exception to raise when API call errors

    Attributes:
        error_code -- HTML response error code to pass back.
        error_source -- value where the error occured.
    """

    def __init__(self, error_code, error_source):
        self.error_code = error_code
        self.error_source = error_source