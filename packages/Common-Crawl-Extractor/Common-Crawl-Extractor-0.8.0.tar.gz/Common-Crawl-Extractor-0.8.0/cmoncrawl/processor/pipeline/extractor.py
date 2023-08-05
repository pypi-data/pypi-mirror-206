from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict

from bs4 import BeautifulSoup

from cmoncrawl.common.types import PipeMetadata
from cmoncrawl.common.loggers import metadata_logger


class BaseExtractor(ABC):
    ENCODING: str | None = None
    SINCE: datetime | None = None
    TO: datetime | None = None

    def __init__(self):
        pass

    def filter_raw(self, response: str, metadata: PipeMetadata) -> bool:
        # If raw fails bs4 will not be used -> speed
        return True

    def filter_soup(self, soup: BeautifulSoup, metadata: PipeMetadata) -> bool:
        # slow but has more info
        return True

    def extract(self, response: str, metadata: PipeMetadata) -> Dict[Any, Any] | None:
        if self.filter_raw(response, metadata) is False:
            metadata_logger.warn(
                "Droped due to raw filter", extra={"domain_record": metadata.domain_record}
            )
            return None

        article = self.preprocess(response, metadata)
        soup = BeautifulSoup(article, "html.parser")
        if self.filter_soup(soup, metadata) is False:
            metadata_logger.warn(
                "Droped due to soup filter", extra={"domain_record": metadata.domain_record}
            )
            return None

        return self.extract_soup(soup, metadata)

    @abstractmethod
    def extract_soup(
        self, soup: BeautifulSoup, metadata: PipeMetadata
    ) -> Dict[Any, Any] | None:
        raise NotImplementedError()

    def preprocess(self, response: str, metadata: PipeMetadata) -> str:
        linux = response.replace("\r\n", "\n")
        # Sorted set pythonic way
        encodings: Dict[str, int] = {}
        if self.ENCODING is not None:
            encodings[self.ENCODING] = 1
        if metadata.domain_record.encoding is not None:
            encodings[metadata.domain_record.encoding] = 1
        http_split = metadata.http_header.get("Content-Type", "").split("charset=")
        if len(http_split) > 1 and http_split[1] != "":
            encodings[http_split[-1]] = 1

        # Fallbacks
        encodings["utf-8"] = 1

        encoded = linux.encode(metadata.encoding)
        for encoding in encodings:
            try:
                decoded = encoded.decode(encoding)
                metadata.encoding = encoding
                break
            except ValueError:
                metadata_logger.warn(
                    f"Failed to decode with {encoding}",
                    extra={"domain_record": metadata.domain_record},
                )
        else:
            raise ValueError("Failed to decode")

        return decoded

class HTMLExtractor(BaseExtractor):
    """
    Dummy Extractor which simply extracts the html
    """
    def extract_soup(self, soup: BeautifulSoup, metadata: PipeMetadata):
        metadata.name = metadata.domain_record.url.replace("/", "_")[:100]
        return {"html": str(soup)}

    def filter_raw(self, response: str, metadata: PipeMetadata):
        if metadata.http_header.get("http_response_code", 200) != 200:
            metadata_logger.warning(
                f"Status: {metadata.http_header.get('http_response_code', 0)}",
                extra={"domain_record": metadata.domain_record},
            )
            return False
        return True