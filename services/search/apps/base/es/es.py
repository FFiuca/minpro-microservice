from config import es

class ESBase():
    client = None

    def __init__(self) -> None:
        self.client = es.client

        # print(self.client)
