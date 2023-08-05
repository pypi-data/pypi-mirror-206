from dataclasses import dataclass
from http import HTTPStatus

import httpx
from bs4 import BeautifulSoup
from validators import url

from .headers import SimpleResponseHeaders
from .meta import SimpleMeta
from .url import ParsedURL


@dataclass
class InspectedURL:
    url: str
    head: httpx.Headers | None = None
    content: bytes | None = None

    def __post_init__(self):
        if not url(
            value=self.url,  # type: ignore
            may_have_port=False,
            simple_host=True,
            skip_ipv6_addr=True,
            skip_ipv4_addr=True,
        ):
            raise Exception(f"Invalid {self.url}")
        r = httpx.get(self.url, follow_redirects=True)
        if not r.status_code == HTTPStatus.OK:
            raise Exception(f"Bad {self.url}: {r.status_code}")
        self.head = r.headers
        self.content = r.content

    @property
    def site_url(self) -> ParsedURL:
        """Wrapper over urlparse.ParsedResult to conform with headers / meta.

        Returns:
            ParsedURL: Fields are from urlparse.ParsedResult
        """
        return ParsedURL.from_url(url=self.url)

    @property
    def site_headers(self) -> SimpleResponseHeaders | None:
        """After an http request is made from the inspected url, extract selected
        response headers. Requires content-type to include `text/html`.

        Returns:
            SimpleResponseHeaders | None: _description_
        """
        if self.head:
            return SimpleResponseHeaders.from_raw_headers(data=self.head)

    @property
    def site_meta(self) -> SimpleMeta | None:
        """Based on content of the url requested, extract meta tags.

        Returns:
            SimpleMeta | None: e.g. title, author, meta tags from html page.
        """
        if self.content:
            return SimpleMeta.from_soup(
                BeautifulSoup(self.content, "html.parser")
            )
