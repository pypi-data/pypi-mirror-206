from pathlib import Path
from typing import List, Set
from cmoncrawl.aggregator.index_query import IndexAggregator
from cmoncrawl.processor.pipeline.pipeline import ProcessorPipeline
from cmoncrawl.common.types import DomainRecord
from cmoncrawl.common.loggers import all_purpose_logger
from cmoncrawl.aggregator.utils.helpers import unify_url_id


async def index_and_extract(
    index_agg: IndexAggregator,
    pipeline: ProcessorPipeline,
    filter_non_unique_url: bool = False,
):
    processed_urls: Set[str] = set()

    if hasattr(pipeline.downloader, "__aenter__"):
        await pipeline.downloader.__aenter__()
    try:
        async with index_agg:
            async for domain_record in index_agg:
                if (
                    filter_non_unique_url
                    and unify_url_id(domain_record.url) in processed_urls
                ):
                    continue
                try:
                    paths: List[Path] = await pipeline.process_domain_record(
                        domain_record
                    )
                    if paths:
                        all_purpose_logger.info(
                            f"Processed {domain_record.url} with {len(paths)} processors"
                        )
                except KeyboardInterrupt as e:
                    break

                except Exception as e:
                    all_purpose_logger.error(
                        f"Failed to process {domain_record.url} with {e}"
                    )
                    continue
                processed_urls.add(unify_url_id(domain_record.url))

    finally:
        if hasattr(pipeline.downloader, "__aexit__"):
            await pipeline.downloader.__aexit__(None, None, None)


async def extrac_from_indexes(
    indexes: List[DomainRecord],
    pipeline: ProcessorPipeline,
):
    if hasattr(pipeline.downloader, "__aenter__"):
        await pipeline.downloader.__aenter__()
    try:
        for domain_record in indexes:
            try:
                paths: List[Path] = await pipeline.process_domain_record(domain_record)
                if paths:
                    all_purpose_logger.info(
                        f"Processed {domain_record.url} with {len(paths)} processors"
                    )
            except KeyboardInterrupt as e:
                break

            except Exception as e:
                all_purpose_logger.error(
                    f"Failed to process {domain_record.url} with {e}"
                )
                continue
    finally:
        if hasattr(pipeline.downloader, "__aexit__"):
            await pipeline.downloader.__aexit__(None, None, None)
