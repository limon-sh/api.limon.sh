import threading


class MetaInformation(threading.local):
    """
    Saving meta information from middlewares

    Middleware cannot store information directly in the request,
    so the storage of the current request execution thread is used.
    """

    def __init__(self):
        self.app_type = None
        self.app_version = None
        self.app_platform = None


meta = MetaInformation()
