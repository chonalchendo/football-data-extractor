import polars as pl

class TransfermarktPolarsPipeline:
    def __init__(self) -> None:
        self.data = []

    def process_item(self, item, spider):
        self.data.append(item)
        return item

    def close_spider(self, spider) -> pl.DataFrame:
        df = pl.DataFrame(self.data)
        return df 


    
