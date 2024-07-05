from config import es

class ESBase():
    client = None
    default = {
        'body': {
            'settings': {
                'number_of_shards': 3,
                'number_of_replicas': 1
            }
        }
    }

    def __init__(self) -> None:
        self.client = es.client

        # print(self.client)
