from man_user.function.kong.kong import KongBase
from config.kong import (
    LISTENER_HOST,
    LISTENER_PORT,
    PATH_GUEST,
    PATH_USER,
)

class ManUserProvider(KongBase):
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

        self.svc = svc
