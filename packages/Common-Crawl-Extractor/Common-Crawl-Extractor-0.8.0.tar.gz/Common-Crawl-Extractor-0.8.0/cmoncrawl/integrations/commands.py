from datetime import datetime
import json
import logging
import os
from pathlib import Path
from cmoncrawl.aggregator.index_query import IndexAggregator

from cmoncrawl.processor.pipeline.downloader import DownloaderDummy, AsyncDownloader
from cmoncrawl.processor.pipeline.pipeline import ProcessorPipeline
from cmoncrawl.processor.pipeline.streamer import OutStreamerFileHTML
from cmoncrawl.processor.pipeline.extractor import HTMLExtractor
from cmoncrawl.middleware.synchronized import index_and_extract


import argparse
from typing import List
import asyncio
from cmoncrawl.processor.pipeline.streamer import (
    OutStreamerFileJSON,
)

from cmoncrawl.processor.pipeline.router import Router
from cmoncrawl.common.loggers import (
    all_purpose_logger,
    metadata_logger,
)
from cmoncrawl.common.types import DomainRecord

async def article_process(
    article_path: List[Path],
    output_path: Path,
    config_path: Path,
    url: str | None,
    date: datetime | None,
):
    with open(config_path, "r") as f:
        config = json.load(f)
    router = Router()
    extractors_path = config.get("extractors_path")
    if extractors_path is not None:
        extractors_path = config_path.parent / extractors_path
    else:
        extractors_path = Path(__file__).parent / "UserDefined"

    router.load_modules(extractors_path)
    router.register_routes(config.get("routes", []))
    downloader = DownloaderDummy(article_path, url, date)
    outstreamer = OutStreamerFileJSON(root=output_path, pretty=True, order_num=False)
    pipeline = ProcessorPipeline(router, downloader, outstreamer)
    # Will be changed anyway
    dummy_record = DomainRecord("", "", 0, 0)
    for path in article_path:
        created_paths = await pipeline.process_domain_record(dummy_record)
        if len(created_paths) == 0:
            continue
        created_path = created_paths[0]
        os.rename(created_path, created_path.parent / (path.stem + ".json"))



def run_process():
    parser = argparse.ArgumentParser(description="Download articles")
    parser.add_argument("article_path", nargs="+", type=Path)
    parser.add_argument("output_path", type=Path)
    parser.add_argument(
        "--config_path",
        type=Path,
        default=Path(__file__).parent / "UserDefined" / "config.json",
    )
    parser.add_argument("--date", type=str)
    parser.add_argument("--url", type=str)
    args = vars(parser.parse_args())
    if isinstance(args["date"], str):
        args["date"] = datetime.fromisoformat(args["date"])
    all_purpose_logger.setLevel(logging.DEBUG)
    metadata_logger.setLevel(logging.DEBUG)

    asyncio.run(article_process(**args))



# ==================================================================================================




async def article_download(
    url: str,
    output: Path,
    cc_server: str | None = None,
    since: datetime = datetime.min,
    to: datetime = datetime.max,
    limit: int = 5,
):
    router = Router()
    router.load_extractor("dummy_extractor", HTMLExtractor())
    router.register_route("dummy_extractor", [r".*"])
    outstreamer = OutStreamerFileHTML(root=output)
    pipeline = ProcessorPipeline(router, AsyncDownloader(), outstreamer)

    index_agg = IndexAggregator(cc_servers=([cc_server] if cc_server else []),
                                domains=[url],
                                since=since,
                                to=to,
                                limit=limit
    )
    await index_and_extract(index_agg, pipeline)


                                


def run_download():
    parser = argparse.ArgumentParser(description="Download articles")
    parser.add_argument("url")
    parser.add_argument("output", type=Path)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--since", type=str, default=datetime.min)
    parser.add_argument("--to", type=str, default=datetime.max)
    parser.add_argument("--encoding", type=str, default="utf-8")
    args = vars(parser.parse_args())
    if isinstance(args["since"], str):
        args["since"] = datetime.fromisoformat(args["since"])

    if isinstance(args["to"], str):
        args["to"] = datetime.fromisoformat(args["to"])

    asyncio.run(article_download(**args))