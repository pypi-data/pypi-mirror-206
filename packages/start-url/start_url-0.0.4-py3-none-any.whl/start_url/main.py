from dataclasses import asdict, dataclass
from http import HTTPStatus
from typing import Any

import httpx
from bs4 import BeautifulSoup

from .headers import SimpleResponseHeaders
from .meta import SimpleMeta
from .url import ParsedURL


@dataclass
class InspectedURL:
    url: str
    head: httpx.Headers | None = None
    content: bytes | None = None

    def __post_init__(self):
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

    def convert(self) -> dict[str, Any]:
        """Convert url, header, meta dataclasses key-value into a single dict.

        Returns:
            dict[str, Any]: Compiled dict of dataclasses, each key is a classname
        """
        data = {}
        for dc in [self.site_url, self.site_headers, self.site_meta]:
            if dc is not None:
                data[dc.__class__.__name__] = asdict(dc)
        return data
