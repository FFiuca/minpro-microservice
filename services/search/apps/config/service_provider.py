from config.kong import KongBase
from django.conf import settings
from config.kong import (
    LISTENER_HOST,
    LISTENER_PORT,
    PATH_GUEST,
    PATH_USER,
)

class ManUserProvider(KongBase):
    host_main = 'http://127.0.0.1:8801'
    svc_name = 'man_user'
    svc_path = 'man_user'

    def __init__(self) -> None:
        super().__init__()

        svc = {}
        svc['url_guest'] = '{host}:{port}/{svc}/{path}'.format(
            host=LISTENER_HOST,
            port=LISTENER_PORT,
            svc=self.svc_path,
            path=PATH_GUEST
        )

        svc['url_user'] = '{host}:{port}/{svc}/{path}'.format(
            host=LISTENER_HOST,
            port=LISTENER_PORT,
            svc=self.svc_path,
            path=PATH_USER
        )

        svc['host_main'] = self.host_main

        self.svc = svc

class MediaProvider(KongBase):
    host_main = 'http://127.0.0.1:8802'
    svc_name = 'media'
    svc_path = 'media'

    def __init__(self) -> None:
        super().__init__()

        svc = {}
        svc['url_guest'] = '{host}:{port}/{svc}/{path}'.format(
            host=LISTENER_HOST,
            port=LISTENER_PORT,
            svc=self.svc_path,
            path=PATH_GUEST
        )

        svc['url_user'] = '{host}:{port}/{svc}/{path}'.format(
            host=LISTENER_HOST,
            port=LISTENER_PORT,
            svc=self.svc_path,
            path=PATH_USER
        )

        svc['host_main'] = self.host_main

        self.svc = svc


class SearchProvider(KongBase):
    host_main = settings.APP_URL
    svc_name = 'media'
    svc_path = 'media'

    def __init__(self) -> None:
        super().__init__()

        svc = {}
        svc['url_guest'] = '{host}:{port}/{svc}/{path}'.format(
            host=LISTENER_HOST,
            port=LISTENER_PORT,
            svc=self.svc_path,
            path=PATH_GUEST
        )

        svc['url_user'] = '{host}:{port}/{svc}/{path}'.format(
            host=LISTENER_HOST,
            port=LISTENER_PORT,
            svc=self.svc_path,
            path=PATH_USER
        )

        svc['host_main'] = self.host_main

        self.svc = svc
