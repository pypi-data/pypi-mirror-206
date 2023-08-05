from dataclasses import dataclass
from urllib.parse import urlparse

from validators import domain


@dataclass
class ParsedURL:
    scheme: str
    netloc: str
    path: str | None = None
    params: str | None = None
    query: str | None = None
    fragment: str | None = None

    @classmethod
    def from_url(cls, url: str):
        p = urlparse(url)
        if domain(p.netloc):  # type: ignore
            return cls(
                scheme=p.scheme,
                netloc=p.netloc,
                path=p.path.removeprefix("/").removesuffix("/") or None,
                params=p.params or None,
                query=p.query or None,
                fragment=p.fragment or None,
            )
        raise Exception(f"Invalid {p.netloc}")

    @property
    def id(self):
        return {
            "domain": self.netloc,
            "route": self.path,
        }

    @property
    def extra(self):
        return {
            "scheme": self.scheme,
            "params": self.params,
            "fragment": self.fragment,
        }
