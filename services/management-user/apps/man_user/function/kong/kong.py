from config.kong import HOST, PORT, URL_MAPPING

class KongBase:
    def __init__(self) -> None:
        self.url = '{}:{}'.format(HOST, PORT)
