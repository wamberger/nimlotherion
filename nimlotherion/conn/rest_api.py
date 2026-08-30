

__all__ = ['RESTapiSession']


from requests import Session
from requests import Response
from requests import PreparedRequest

from nimlotherion.utils.crypto import CryptoSafe


type resp = tuple[bool, Response, str] | tuple[bool, Response]


class RESTapiSession[resp]:
    def __init__(
            self,
            domain: str = None,
            path: str = None,
            headers: dict = None,
            params: str = None,
            user: str = None,
            password: str = None,
            encoding: str = 'UTF-8') -> None:

        """
        domain: scheme + domain + port
        params: parameters | parameters + anchor
        """

        self.session: Session = Session()

        self.encoding = encoding
        self.domain = domain
        self.path = path
        self.params = params
        self.key = None  # currently not used
        self.token = None  # currently not used

        if path is not None:
            self.path = CryptoSafe(bytes(path, encoding))
        if params is not None:
            self.params = CryptoSafe(bytes(params, encoding))
        if headers is not None:
            self.session.headers.update(headers)
        if user and password is not None:
            self.session.auth = (user, password)

    def update_headers(self, param: dict) -> None:
        self.session.headers.update(param)

    def update_params(self, params: str) -> None:
        self.params = CryptoSafe(bytes(params, self.encoding))

    def update_path(self, path: str) -> None:
        self.path = CryptoSafe(bytes(path, self.encoding))

    def update_domain(self, domain: str) -> None:
        self.domain = domain

    def prepped(self, prepped: PreparedRequest, **kwargs) -> Response:
        return self.session.send(prepped, **kwargs)

    def get(self, url: str = None, **kwargs) -> resp:
        if url:
            return self.response(self.session.get(url, **kwargs))
        else:
            return self.response(self.session.get(self.get_url(), **kwargs))

    def post(self, url: str = None, **kwargs) -> resp:
        if url:
            return self.response(self.session.post(url, **kwargs))
        else:
            return self.response(
                self.session.post(self.get_url(), **kwargs))

    def put(self, url: str, **kwargs) -> resp:
        if url:
            return self.response(self.session.put(url, **kwargs))
        else:
            return self.response(self.session.put(self.get_url(), **kwargs))

    def delete(self, url: str, **kwargs) -> resp:
        if url:
            return self.response(self.session.delete(url, **kwargs))
        else:
            return self.response(self.session.delete(self.get_url(), **kwargs))

    def head(self, url: str, **kwargs) -> Response:
        return self.session.head(url, **kwargs)

    def options(self, url: str, **kwargs) -> Response:
        return self.session.options(url, **kwargs)

    def get_url(self) -> str:
        if self.domain and self.path and self.params:
            path = self.path.decrypt().decode(self.encoding)
            params = self.params.decrypt().decode(self.encoding)
            return f"{self.domain}{path}{params}"
        elif self.domain and self.path:
            path = self.path.decrypt().decode(self.encoding)
            return f"{self.domain}{path}"
        elif self.domain:
            return f"{self.domain}"
        else:
            return ""

    @staticmethod
    def response(response: Response) -> resp:
        code = response.status_code
        text: str = (f"{code}"
                     f"{response.reason}: "
                     f"{response.text}. "
                     f"url:{response.url}")
        if 200 <= code <= 299:
            return True, response
        else:
            return False, response, text
