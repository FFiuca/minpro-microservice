from django.conf import settings
from man_user.function.kong.kong import KongBase
from urllib.parse import urlparse, ParseResult

def switch_to_kong_host(url: str):
    url= urlparse(url)
    # print('switch_to_kong_host', url)
    host= url.netloc
    host= '{}{}'.format(url.scheme+'://' if bool(url.scheme) else '', host)
    if host=='':
        return KongBase().listener_url+ url.geturl()

    return url.geturl().replace(host, KongBase().listener_url)
