import scrapy

# TODO

class AltaSpider(scrapy.Spider):
    name = "alta"
    allowed_domains = ["alta.ge"]
    search_term = "xbox"
    start_urls = [f"https://alta.ge/?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&q={search_term}&dispatch=products.search&items_per_page=1000"]
    handle_httpstatus_list = [403]

    def parse(self, response):
        pass
