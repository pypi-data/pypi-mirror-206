from sidetrek.core.types import SidetrekIterDataset
from torchdata.datapipes.iter import IterableWrapper


def build_datapipes(io: str, source: str, options: dict) -> SidetrekIterDataset:
    if io == 's3':
        region = options["region"] or "us-west-1"
        buffer_size = options["buffer_size"] or 128
        
        dp_s3_urls = IterableWrapper([source]).list_files_by_s3()
        sharded_s3_urls = dp_s3_urls.shuffle().sharding_filter()
        dp_s3_files = sharded_s3_urls.load_files_by_s3(region=region, buffer_size=buffer_size)
    
    return


def load_dataset():
    return 